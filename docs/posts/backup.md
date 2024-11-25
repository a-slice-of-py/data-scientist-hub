---
date: 2024-04-05
authors:
  - silvio
categories:
  - Solutions
tags:
  - Python
---

# Backup script for disaster recovery

After having accidentally deleted _every browser bookmark saved in more than 5 years of work_, I decided to write down a simple backup script to prevent such a disaster from happening again.

<!-- more -->

The final solution includes:

- browser bookmarks
- Windows Terminal settings
- [cmder](https://cmder.app/) aliases
- Visual Studio Code extensions

Everything is then versioned in a Git repo, together all my notes (taken via [Obsidian](https://obsidian.md/)).

```python
import shutil
import subprocess
from pathlib import Path

TARGET_PATH = Path(...).resolve()

paths = (
    "%USERPROFILE%/AppData/Local/Microsoft/Edge/User Data/Default/Bookmarks",
    "%USERPROFILE%/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json",
    "%USERPROFILE%/Documents/projects/cmder_mini/config/user_aliases.cmd",
    "%USERPROFILE%/Documents/projects/cmder_mini/config/.history",
)

def main() -> None:
    for path in paths:
        shutil.copy(path, TARGET_PATH)

    with open(f"{TARGET_PATH}/vsc_extensions.txt", "w") as f:
        response = subprocess.run(
            [
                "code",
                "--list-extensions",
                "--show-versions",
            ],
            shell=True,
            capture_output=True,
            text=True,
            check=True,
        )
        f.write(response.stdout)

if __name__ == "__main__":
    main()
```
