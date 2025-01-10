import os
import subprocess
from collections import defaultdict
from datetime import datetime
from typing import Optional

NEWLINE = "\n"
RESOURCES_PATH = "docs/resources"


def get_added_lines(start: Optional[str] = None, end: Optional[str] = None):
    blacklist = ("about.md", "index.md")
    # Get the list of files changed in the last commit
    files_changed = subprocess.check_output(
        ["git", "show", "-U0", "--pretty=", "--name-only", end],
        universal_newlines=True,
    ).splitlines()

    added_lines = defaultdict(list)

    for filename in files_changed:
        if (
            filename.endswith(".md")
            and ("/resources/" in filename)
            and all(not filename.endswith(name) for name in blacklist)
        ):
            # Get the diff for each file
            diff_output = subprocess.check_output(
                ["git", "diff", start, end, "--", filename],
                universal_newlines=True,
                encoding="utf-8",
            ).splitlines()

            # Extract added lines
            for line in diff_output:
                if (
                    line.startswith("+")
                    and not line.startswith("+++")
                    and line.replace("+", "").replace(" ", "")
                    and not line.startswith("+#")
                ):
                    added_lines[filename].append(line[1:])

    return added_lines


def update_resources_changelog(
    date: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None
) -> None:
    if date is None:
        date = str(datetime.now().date())
    if end is None:
        start, end = "HEAD^", "HEAD"

    added_lines = get_added_lines(start, end)
    titles = {}
    for filename in added_lines:
        try:
            with open(filename, "r") as f:
                titles[filename] = f.readlines()[0]
        except FileNotFoundError:
            pass
    added_lines = {k: v for k, v in added_lines.items() if k in titles}
    changelog = [f"# {date}\n\n"]
    for filename, lines in sorted(added_lines.items(), key=lambda x: titles[x[0]]):
        changelog.append(f"#{titles[filename]}\n")
        changelog.append("\n<!-- --8<-- [start:body] -->\n")
        for line in sorted(lines):
            changelog.append(f"{line}\n")
        changelog.append("\n<!-- --8<-- [end:body] -->\n")
        changelog.append("\n")
    with open(f"./docs/resources/changelog/{date}.md", "w", encoding="utf-8") as f:
        f.writelines(changelog[:-1])

    with open(
        f"./docs/posts/resources_{date.replace('-', '_')}.md", "w", encoding="utf-8"
    ) as f:
        post_lines = [
            "---\n",
            f"date: {date}\n",
            "authors:\n",
            "- silvio\n",
            "categories:\n",
            "- Resources\n",
            "---\n",
            "\n# (my) Hacker News #7\n",
            "\nHere's a list of the latest resources that grabbed my attention.\n",
            "\n<!-- more -->\n",
            f'\n--8<-- "docs/resources/changelog/{date}.md:body"\n',
        ]
        f.writelines(post_lines)


def update_resources_index(*args, **kwargs) -> None:
    """Create index for each of the resources sections."""
    blacklist = (".pages", "index.md", "changelog")
    for section in sorted(os.listdir(RESOURCES_PATH)):
        if section not in blacklist:
            section_name = (
                section.replace("-", " ").title() if section.lower() != "aws" else "AWS"
            )
            index = [f"# {section_name}", NEWLINE, NEWLINE]
            path = f"{RESOURCES_PATH}/{section}"
            for file in sorted(os.listdir(path)):
                if file not in blacklist:
                    with open(f"{path}/{file}", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if line.startswith("#"):
                                lines[i] = f"#{line}"
                        index.extend(lines)
                    if index[-1] == NEWLINE or index[-1].endswith(NEWLINE):
                        index.append(NEWLINE)
                    else:
                        index.extend([NEWLINE, NEWLINE])

            with open(f"{path}/index.md", "w", encoding="utf-8") as f:
                f.writelines(index)


if __name__ == "__main__":
    update_resources_index()
