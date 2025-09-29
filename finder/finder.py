from pathlib import Path
import re
import json


def build_index() -> None:
    index = []
    base_path = Path("./docs/resources")
    for folder in base_path.iterdir():
        if "." not in str(folder):
            for filename in folder.glob("index.md"):
                with open(filename, "r", encoding="utf-8") as f:
                    content = [line.replace("\n", "") for line in f.readlines()]
                    content = [line for line in content if line]
                for line in content:
                    line = line.strip()
                    h1, h2, h3 = "# ", "## ", "### "
                    if line.startswith(h1):
                        category = line.replace(h1, "")
                        topic, section = None, None
                    if line.startswith(h2):
                        topic = line.replace(h2, "")
                        section = None
                    if line.startswith(h3):
                        section = line.replace(h3, "")
                    if line.startswith("- ["):
                        # Extract link name and URL using regex
                        match = re.match(r"- \[([^\]]+)\]\(([^)]+)\)", line)
                        if match:
                            link_name = match.group(1)
                            url = match.group(2)
                            index.append(
                                {
                                    "category": category,
                                    "topic": topic,
                                    "section": section,
                                    "link_name": link_name,
                                    "url": url,
                                }
                            )
    with open("./finder/index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


def main() -> None:
    # if not os.path.exists("./index.json"):
    #     build_index()
    build_index()


if __name__ == "__main__":
    main()
