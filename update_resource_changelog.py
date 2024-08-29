import subprocess
from collections import defaultdict
from datetime import datetime

blacklist = ("about.md", "index.md")


def get_added_lines():
    # Get the list of files changed in the last commit
    files_changed = subprocess.check_output(
        ["git", "show", "-U0", "--pretty=", "--name-only", "HEAD"],
        universal_newlines=True,
    ).splitlines()

    added_lines = defaultdict(list)

    for filename in files_changed:
        if all(not filename.endswith(name) for name in blacklist):
            # Get the diff for each file
            diff_output = subprocess.check_output(
                ["git", "diff", "HEAD^", "HEAD", "--", filename],
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


if __name__ == "__main__":
    added_lines = get_added_lines()
    titles = {}
    for filename in added_lines:
        with open(filename, "r") as f:
            titles[filename] = f.readlines()[0]
    today = str(datetime.now().date())
    changelog = [f"# {today}\n\n"]
    # TODO: sort filename by titles
    for filename, lines in sorted(added_lines.items(), key=lambda x: titles[x[0]]):
        changelog.append(f"#{titles[filename]}\n")
        for line in sorted(lines):
            changelog.append(f"{line}\n")
        changelog.append("\n")
    with open(f"./docs/resources/changelog/{today}.md", "w", encoding="utf-8") as f:
        f.writelines(changelog[:-1])
