import os

NEWLINE = "\n"
BLACKLIST = (".pages", "index.md")
RESOURCES_PATH = "docs/resources"


def _index_resources(*args, **kwargs) -> None:
    """Create index for each of the resources sections."""
    for section in sorted(os.listdir(RESOURCES_PATH)):
        if section not in BLACKLIST:
            section_name = (
                section.replace("-", " ").title() if section.lower() != "aws" else "AWS"
            )
            index = [f"# {section_name}", NEWLINE, NEWLINE]
            path = f"{RESOURCES_PATH}/{section}"
            for file in sorted(os.listdir(path)):
                if file not in BLACKLIST:
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
    _index_resources()
