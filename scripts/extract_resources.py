"""Extract content from all resource links listed in finder/public/index.json.

For each link, fetches the page content and extracts the main text:
- GitHub repos: uses the GitHub API (description + README)
- Everything else: uses trafilatura for boilerplate-free extraction

Results are saved to docs/raw/{category}/{topic}/{slug}.md with YAML frontmatter.
Progress is checkpointed in .cache/extract_manifest.jsonl for pause/resume.

Usage:
  uv run scripts/extract_resources.py --dry-run
  uv run scripts/extract_resources.py --category python --limit 50
  uv run scripts/extract_resources.py --retry-failed
"""

# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx[http2]",
#   "trafilatura",
#   "python-slugify",
#   "truststore",
#   "python-dotenv",
# ]
# ///

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
import time
from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()  # Load .env file (GH_TOKEN, etc.)

import httpx
import trafilatura
import truststore

# Use the OS certificate store (includes corporate proxy CA certs)
truststore.inject_into_ssl()

from slugify import slugify

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

INDEX_JSON = Path(__file__).resolve().parent.parent / "finder" / "public" / "index.json"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "raw"
CACHE_DIR = Path(__file__).resolve().parent.parent / ".cache"
MANIFEST_PATH = CACHE_DIR / "extract_manifest.jsonl"

GITHUB_REPO_PATTERN = re.compile(
    r"https?://github\.com/([A-Za-z0-9\-_.]+)/([A-Za-z0-9\-_.]+)/?$"
)

# Domains known to block scrapers or require subscription
PAYWALL_DOMAINS = {
    "towardsdatascience.com",
    "medium.com",
    "pub.towardsai.net",
    "levelup.gitconnected.com",
    "betterprogramming.pub",
    "python.plainenglish.io",
    "ai.gopubby.com",
    "blog.serverlessadvocate.com",
}

BROKEN_STATUS_CODES = {404, 410, 451}  # Not Found, Gone, Unavailable For Legal Reasons

DEFAULT_CONCURRENCY = 10
DEFAULT_DELAY = 1.0
README_MAX_CHARS = 4000

USER_AGENT = (
    "Mozilla/5.0 (compatible; resource-extractor/1.0; "
    "+https://github.com/data-scientist-hub)"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class Reference:
    category: str
    topic: str
    section: str | None = None


class PaywallError(Exception):
    """Raised when a known paywall domain returns no extractable content."""


@dataclass
class ResourceLink:
    url: str
    label: str
    references: list[Reference]

    @property
    def primary(self) -> Reference:
        """First reference is used for output path and filtering."""
        return self.references[0]


@dataclass
class ManifestEntry:
    url: str
    label: str
    category: str
    topic: str
    status: str  # "done" | "broken" | "paywall" | "empty" | "failed"
    method: str  # "github" | "trafilatura" | "skip"
    output: str  # relative path to output file
    status_code: int | None = None
    error: str | None = None
    ts: str = ""


# ---------------------------------------------------------------------------
# Parsing index.json
# ---------------------------------------------------------------------------


def discover_all_links() -> list[ResourceLink]:
    """Load all links from finder/public/index.json, grouping references per URL."""
    raw = json.loads(INDEX_JSON.read_text(encoding="utf-8"))

    # Group all (category, topic, section) tuples by URL
    url_refs: dict[str, list[Reference]] = {}
    url_labels: dict[str, str] = {}

    for entry in raw:
        url = entry["url"].strip()
        ref = Reference(
            category=entry["category"].strip(),
            topic=entry["topic"].strip() if entry.get("topic") else "uncategorized",
            section=entry.get("section"),
        )
        if url not in url_refs:
            url_refs[url] = []
            url_labels[url] = entry["link_name"].strip()
        url_refs[url].append(ref)

    all_links = [
        ResourceLink(url=url, label=url_labels[url], references=refs)
        for url, refs in url_refs.items()
    ]

    return all_links


# ---------------------------------------------------------------------------
# Manifest (checkpoint) management
# ---------------------------------------------------------------------------


def load_manifest() -> dict[str, ManifestEntry]:
    """Load existing manifest entries, keyed by URL. Last entry wins (for retries)."""
    entries: dict[str, ManifestEntry] = {}
    if not MANIFEST_PATH.exists():
        return entries

    for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            entries[data["url"]] = ManifestEntry(**data)
        except (json.JSONDecodeError, TypeError, KeyError) as exc:
            log.warning("Skipping malformed manifest line: %s", exc)

    return entries


def append_manifest(entry: ManifestEntry) -> None:
    """Append a single entry to the manifest file (crash-safe)."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with MANIFEST_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Output writing
# ---------------------------------------------------------------------------


def build_output_path(link: ResourceLink) -> Path:
    """Build the output path: docs/raw/{category}/{topic_slug}/{label_slug}.md"""
    ref = link.primary
    category_slug = slugify(ref.category, max_length=60)
    topic_slug = slugify(ref.topic, max_length=60)
    label_slug = slugify(link.label, max_length=80)
    if not label_slug:
        label_slug = slugify(link.url.split("/")[-1], max_length=80) or "untitled"
    return OUTPUT_DIR / category_slug / topic_slug / f"{label_slug}.md"


def write_output(path: Path, link: ResourceLink, method: str, content: str) -> None:
    """Write extracted content with YAML frontmatter."""
    path.parent.mkdir(parents=True, exist_ok=True)

    # Build references block
    refs_lines = []
    for ref in link.references:
        parts = [f"category: {ref.category}", f"topic: {ref.topic}"]
        if ref.section:
            parts.append(f"section: {ref.section}")
        refs_lines.append("  - {" + ", ".join(parts) + "}")

    frontmatter = (
        f"---\n"
        f"source: {link.url}\n"
        f"label: {link.label}\n"
        f"references:\n"
        + "\n".join(refs_lines) + "\n"
        f"method: {method}\n"
        f"extracted: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}\n"
        f"---\n\n"
    )

    path.write_text(frontmatter + content, encoding="utf-8")


# ---------------------------------------------------------------------------
# GitHub extraction
# ---------------------------------------------------------------------------


async def extract_github(
    client: httpx.AsyncClient, link: ResourceLink, token: str | None
) -> str:
    """Extract content from a GitHub repo using the API."""
    match = GITHUB_REPO_PATTERN.match(link.url)
    if not match:
        raise ValueError(f"Not a valid GitHub repo URL: {link.url}")

    owner, repo = match.group(1), match.group(2)
    repo = repo.rstrip("/")

    headers: dict[str, str] = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Fetch repo metadata
    repo_resp = await client.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers,
    )
    repo_resp.raise_for_status()
    repo_data = repo_resp.json()

    description = repo_data.get("description") or ""
    topics = repo_data.get("topics") or []
    language = repo_data.get("language") or ""
    stars = repo_data.get("stargazers_count", 0)

    # Fetch README
    readme_content = ""
    try:
        readme_resp = await client.get(
            f"https://api.github.com/repos/{owner}/{repo}/readme",
            headers={**headers, "Accept": "application/vnd.github.raw+json"},
        )
        if readme_resp.status_code == 200:
            readme_content = readme_resp.text[:README_MAX_CHARS]
    except httpx.HTTPError:
        pass  # README is optional enrichment

    # Build markdown output
    parts = [f"# {repo}\n"]
    if description:
        parts.append(f"> {description}\n")

    meta_parts = []
    if language:
        meta_parts.append(f"**Language**: {language}")
    if stars:
        meta_parts.append(f"**Stars**: {stars:,}")
    if topics:
        meta_parts.append(f"**Topics**: {', '.join(topics)}")
    if meta_parts:
        parts.append(" | ".join(meta_parts) + "\n")

    if readme_content:
        parts.append(f"\n## README\n\n{readme_content}")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Trafilatura extraction
# ---------------------------------------------------------------------------


async def extract_trafilatura(client: httpx.AsyncClient, link: ResourceLink) -> str:
    """Fetch a URL and extract main content using trafilatura."""
    resp = await client.get(
        link.url,
        follow_redirects=True,
        headers={"User-Agent": USER_AGENT},
    )
    resp.raise_for_status()

    # trafilatura.extract is CPU-bound but fast (~50ms); run in thread to not block
    extracted = await asyncio.to_thread(
        trafilatura.extract,
        resp.text,
        output_format="markdown",
        include_links=True,
        include_formatting=True,
        url=link.url,
        no_fallback=True,
    )

    if not extracted:
        domain = urlparse(link.url).netloc
        if domain in PAYWALL_DOMAINS:
            raise PaywallError(f"Paywall domain returned no extractable content: {link.url}")
        raise ValueError(f"Trafilatura returned empty content for {link.url}")

    return extracted


# ---------------------------------------------------------------------------
# Per-domain rate limiting
# ---------------------------------------------------------------------------


class DomainRateLimiter:
    """Ensures at most one request per `delay` seconds per domain."""

    def __init__(self, delay: float = DEFAULT_DELAY):
        self._delay = delay
        self._locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)
        self._last_request: dict[str, float] = {}

    async def acquire(self, url: str) -> None:
        domain = urlparse(url).netloc
        async with self._locks[domain]:
            last = self._last_request.get(domain, 0.0)
            elapsed = time.monotonic() - last
            if elapsed < self._delay:
                await asyncio.sleep(self._delay - elapsed)
            self._last_request[domain] = time.monotonic()


# ---------------------------------------------------------------------------
# Main processing loop
# ---------------------------------------------------------------------------


async def process_link(
    client: httpx.AsyncClient,
    link: ResourceLink,
    rate_limiter: DomainRateLimiter,
    semaphore: asyncio.Semaphore,
    gh_token: str | None,
) -> ManifestEntry:
    """Process a single link: fetch, extract, write output, return manifest entry."""
    output_path = build_output_path(link)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    async with semaphore:
        await rate_limiter.acquire(link.url)

        try:
            is_github = GITHUB_REPO_PATTERN.match(link.url) is not None

            if is_github:
                content = await extract_github(client, link, gh_token)
                method = "github"
            else:
                content = await extract_trafilatura(client, link)
                method = "trafilatura"

            write_output(output_path, link, method, content)

            return ManifestEntry(
                url=link.url,
                label=link.label,
                category=link.primary.category,
                topic=link.primary.topic,
                status="done",
                method=method,
                output=str(output_path.relative_to(output_path.parents[3])),
                ts=now,
            )

        except httpx.HTTPStatusError as exc:
            code = exc.response.status_code
            if code in BROKEN_STATUS_CODES:
                status = "broken"
            elif code in (401, 402, 403) or (
                code == 200
                and urlparse(link.url).netloc in PAYWALL_DOMAINS
            ):
                status = "paywall"
            else:
                status = "failed"
            return ManifestEntry(
                url=link.url,
                label=link.label,
                category=link.primary.category,
                topic=link.primary.topic,
                status=status,
                method="github" if GITHUB_REPO_PATTERN.match(link.url) else "trafilatura",
                output="",
                status_code=code,
                error=f"HTTP {code}",
                ts=now,
            )

        except (httpx.RequestError, ValueError, PaywallError, OSError) as exc:
            error_msg = f"{type(exc).__name__}: {exc}"
            if isinstance(exc, PaywallError):
                status = "paywall"
            elif isinstance(exc, ValueError):
                status = "empty"
            else:
                status = "failed"
            return ManifestEntry(
                url=link.url,
                label=link.label,
                category=link.primary.category,
                topic=link.primary.topic,
                status=status,
                method="github" if GITHUB_REPO_PATTERN.match(link.url) else "trafilatura",
                output="",
                error=error_msg,
                ts=now,
            )


async def run(
    category: str | None,
    limit: int | None,
    retry_failed: bool,
    concurrency: int,
    delay: float,
    dry_run: bool,
) -> None:
    """Main async entry point."""
    # Discover all links
    all_links = discover_all_links()
    log.info("Discovered %d unique links across all categories.", len(all_links))

    # Filter by category if requested
    if category:
        all_links = [
            lnk for lnk in all_links
            if any(ref.category.lower() == category.lower() for ref in lnk.references)
        ]
        log.info("Filtered to %d links in category '%s'.", len(all_links), category)

    # Load checkpoint
    manifest = load_manifest()
    done_urls = {url for url, entry in manifest.items() if entry.status == "done"}
    failed_urls = {
        url for url, entry in manifest.items() if entry.status != "done"
    }

    # Determine which links to process
    if retry_failed:
        pending = [lnk for lnk in all_links if lnk.url in failed_urls]
        log.info("Retrying %d previously failed links.", len(pending))
    else:
        pending = [lnk for lnk in all_links if lnk.url not in done_urls]
        log.info("%d links pending (%d already done).", len(pending), len(done_urls))

    # Apply limit
    if limit and limit < len(pending):
        pending = pending[:limit]
        log.info("Limited to %d links for this run.", limit)

    # Dry run: just print stats
    if dry_run:
        _print_dry_run_stats(all_links, pending, done_urls, failed_urls)
        return

    if not pending:
        log.info("Nothing to do. All links already processed.")
        return

    # Process
    rate_limiter = DomainRateLimiter(delay=delay)
    semaphore = asyncio.Semaphore(concurrency)
    gh_token = os.environ.get("GH_TOKEN")

    if not gh_token:
        github_count = sum(
            1 for lnk in pending if GITHUB_REPO_PATTERN.match(lnk.url)
        )
        if github_count > 0:
            log.warning(
                "GH_TOKEN not set. GitHub API is limited to 60 req/hr. "
                "Found %d GitHub links to process. Set GH_TOKEN for 5000 req/hr.",
                github_count,
            )

    done_count = 0
    fail_count = 0
    total = len(pending)

    async with httpx.AsyncClient(
        timeout=httpx.Timeout(30.0, connect=10.0),
        follow_redirects=True,
        http2=True,
    ) as client:
        # Process in batches to write checkpoints immediately
        tasks = []
        for link in pending:
            task = asyncio.create_task(
                process_link(client, link, rate_limiter, semaphore, gh_token)
            )
            tasks.append(task)

        for coro in asyncio.as_completed(tasks):
            entry = await coro
            append_manifest(entry)
            if entry.status == "done":
                done_count += 1
            else:
                fail_count += 1
            processed = done_count + fail_count
            log.info(
                "[%d/%d] (%.0f%%) %s | %s",
                processed,
                total,
                processed / total * 100,
                "OK  " if entry.status == "done" else "FAIL",
                entry.label[:50],
            )

    log.info(
        "Run complete: %d succeeded, %d failed out of %d attempted.",
        done_count,
        fail_count,
        total,
    )


def _print_dry_run_stats(
    all_links: list[ResourceLink],
    pending: list[ResourceLink],
    done_urls: set[str],
    failed_urls: set[str],
) -> None:
    """Print statistics without processing anything."""
    print("\n" + "=" * 60)
    print("DRY RUN — Resource Extraction Stats")
    print("=" * 60)
    print(f"  Total unique links:   {len(all_links)}")
    print(f"  Already done:         {len(done_urls)}")
    print(f"  Previously failed:    {len(failed_urls)}")
    print(f"  Pending this run:     {len(pending)}")
    print()

    # Category breakdown
    by_category: dict[str, int] = defaultdict(int)
    for lnk in pending:
        by_category[lnk.primary.category] += 1

    print("  Pending by category:")
    for cat, count in sorted(by_category.items()):
        print(f"    {cat:<25} {count:>4}")

    # GitHub vs other
    github_count = sum(1 for lnk in pending if GITHUB_REPO_PATTERN.match(lnk.url))
    other_count = len(pending) - github_count
    print(f"\n  GitHub repos:         {github_count}")
    print(f"  Other (trafilatura):  {other_count}")

    # Domain distribution (top 10)
    by_domain: dict[str, int] = defaultdict(int)
    for lnk in pending:
        by_domain[urlparse(lnk.url).netloc] += 1
    top_domains = sorted(by_domain.items(), key=lambda x: x[1], reverse=True)[:15]
    print("\n  Top domains:")
    for domain, count in top_domains:
        print(f"    {domain:<40} {count:>4}")

    print("\n" + "=" * 60 + "\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract content from resource links.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--category",
        type=str,
        default=None,
        help="Process only this category (folder name under docs/resources/)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max number of links to process in this run",
    )
    parser.add_argument(
        "--retry-failed",
        action="store_true",
        help="Re-attempt previously failed URLs",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Max concurrent connections (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY,
        help=f"Min delay between requests to same domain in seconds (default: {DEFAULT_DELAY})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show stats without fetching anything",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a report of broken/paywall/empty links from the manifest",
    )

    args = parser.parse_args()

    if args.report:
        _print_report()
        return

    asyncio.run(
        run(
            category=args.category,
            limit=args.limit,
            retry_failed=args.retry_failed,
            concurrency=args.concurrency,
            delay=args.delay,
            dry_run=args.dry_run,
        )
    )


def _print_report() -> None:
    """Print a categorized report of problematic links for cleanup."""
    manifest = load_manifest()
    if not manifest:
        print("No manifest found. Run the extraction first.")
        return

    # Group by status
    by_status: dict[str, list[ManifestEntry]] = defaultdict(list)
    for entry in manifest.values():
        if entry.status != "done":
            by_status[entry.status].append(entry)

    total_problems = sum(len(v) for v in by_status.values())
    if not total_problems:
        print("All processed links are healthy.")
        return

    print("\n" + "=" * 70)
    print("LINK HEALTH REPORT")
    print("=" * 70)
    print(f"  Total problematic: {total_problems}")
    for status, entries in sorted(by_status.items()):
        print(f"  {status:<10}: {len(entries)}")
    print()

    for status in ("broken", "paywall", "empty", "failed"):
        entries = by_status.get(status, [])
        if not entries:
            continue
        print(f"\n{'─' * 70}")
        print(f"  {status.upper()} ({len(entries)} links)")
        print(f"{'─' * 70}")
        for entry in sorted(entries, key=lambda e: (e.category, e.topic, e.url)):
            error_short = f" [{entry.error}]" if entry.error else ""
            print(f"  [{entry.category}/{entry.topic}] {entry.url}{error_short}")

    print("\n" + "=" * 70)
    print("\nTo export as a cleanup list:")
    print(f"  uv run scripts/extract_resources.py --report > broken_links.txt")
    print()


if __name__ == "__main__":
    main()
