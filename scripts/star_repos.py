"""Star all GitHub repos mentioned in docs/resources/**/index.md files.

Requires: GH_TOKEN environment variable set with a personal access token
  (needs 'starring' user permission or 'public_repo' scope for classic tokens).

  Create one at: https://github.com/settings/tokens

Usage:
  python scripts/star_repos.py --dry-run   # preview repos found
  python scripts/star_repos.py             # star them all
"""

import os
import re
import sys
import time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

RESOURCES_DIR = Path(__file__).parent.parent / "docs" / "resources"
GITHUB_REPO_PATTERN = re.compile(
    r"https?://github\.com/([A-Za-z0-9\-_.]+)/([A-Za-z0-9\-_.]+)"
)


def extract_repos(directory: Path) -> set[tuple[str, str]]:
    """Extract unique (owner, repo) pairs from all index.md files."""
    repos: set[tuple[str, str]] = set()
    for md_file in directory.glob("**/index.md"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        for match in GITHUB_REPO_PATTERN.finditer(content):
            owner, repo = match.group(1), match.group(2)
            repo = repo.rstrip("/").split("#")[0].split("?")[0]
            if owner.lower() in ("orgs", "settings", "features", "topics", "explore"):
                continue
            repos.add((owner, repo))
    return repos


def star_repo(owner: str, repo: str, token: str) -> tuple[bool, int]:
    """Star a repo via GitHub API. Returns (success, status_code)."""
    url = f"https://api.github.com/user/starred/{owner}/{repo}"
    req = Request(url, method="PUT")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Length", "0")
    try:
        response = urlopen(req)
        return True, response.status
    except HTTPError as e:
        # 307: repo was renamed/transferred — follow the redirect
        if e.code == 307:
            redirect_url = e.headers.get("Location")
            if redirect_url:
                req2 = Request(redirect_url, method="PUT")
                req2.add_header("Authorization", f"Bearer {token}")
                req2.add_header("Accept", "application/vnd.github+json")
                req2.add_header("Content-Length", "0")
                try:
                    response = urlopen(req2)
                    return True, response.status
                except HTTPError as e2:
                    return False, e2.code
        return False, e.code


def main():
    dry_run = "--dry-run" in sys.argv

    # --only owner/repo owner/repo ... targets specific repos
    # --from-file path/to/file.md reads repos from a file (one owner/repo per line)
    if "--from-file" in sys.argv:
        file_idx = sys.argv.index("--from-file")
        file_path = Path(sys.argv[file_idx + 1])
        repos = set()
        for line in file_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "/" in line and not line.startswith("#"):
                owner, repo = line.split("/", 1)
                repos.add((owner.strip(), repo.strip()))
        print(f"Targeting {len(repos)} repos from {file_path}.\n")
    elif "--only" in sys.argv:
        only_idx = sys.argv.index("--only")
        only_args = sys.argv[only_idx + 1:]
        repos = set()
        for arg in only_args:
            if "/" in arg:
                owner, repo = arg.split("/", 1)
                repos.add((owner, repo))
        print(f"Targeting {len(repos)} specific repos.\n")
    else:
        print(f"Scanning {RESOURCES_DIR} for GitHub repo URLs...")
        repos = extract_repos(RESOURCES_DIR)
        print(f"Found {len(repos)} unique repos.\n")

    if dry_run:
        for owner, repo in sorted(repos):
            print(f"  {owner}/{repo}")
        print("\nDry run complete. Use without --dry-run to star them.")
        return

    token = os.environ.get("GH_TOKEN")
    if not token:
        print("Error: GH_TOKEN environment variable is not set.")
        print()
        print("Set it with a personal access token:")
        print("  PowerShell:  $env:GH_TOKEN = 'ghp_...'")
        print("  cmd:         set GH_TOKEN=ghp_...")
        print()
        print("Create one at: https://github.com/settings/tokens")
        print("  - Fine-grained: enable 'Starring' user permission (write)")
        print("  - Classic: check 'public_repo' scope")
        sys.exit(1)

    starred = 0
    skipped = 0
    failed = 0
    for owner, repo in sorted(repos):
        success, status = star_repo(owner, repo, token)
        if success and status == 204:
            starred += 1
            print(f"  ★ {owner}/{repo}")
        elif success and status == 304:
            skipped += 1
            print(f"  · {owner}/{repo} (already starred)")
        else:
            failed += 1
            print(f"  ✗ {owner}/{repo} (HTTP {status})")
        time.sleep(0.3)

    print(f"\nDone: {starred} starred, {skipped} already starred, {failed} failed.")


if __name__ == "__main__":
    main()
