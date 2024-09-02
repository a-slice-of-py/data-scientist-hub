---
date: 2024-02-15
authors:
  - silvio
categories:
  - Solutions
tags:
  - Python
  - mkdocs
---

# A homemade replacement for `mkdocstrings`

In these days I am tidying up the documentation of a legacy codebase, where "legacy" stands for something in between [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code) and _"things I wish I've done differently"_. Since I wish the output of the work to be as much complete as possible, I decided to include also the source code in the new docs built with [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

The go-to choice could have been [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings), but I wanted to avoid some setup complexity[^1] so I wrote down a custom source code collector.

<!-- more -->

```python title="source_code_collector.py" linenums="1" hl_lines="52 57 58"
import os
import shutil
from collections import defaultdict
from typing import List

target_dir: str = ... # should be a docs/ subfolder, e.g. "docs/code"
folders_to_skip: List[str] = ...
filenames_to_include: List[str] = ...
filenames_to_exclude: List[str] = ...
extensions_to_collect: List[str] = ... # e.g. ["py", "yaml", "Dockefile"]


def walk(path: str) -> List[str]:
    response = [
        f"{base}/{f}"
        for base, _, files in os.walk(path)
        for f in files
        if all(path not in base for path in folders_to_skip)
        and all(path not in f for path in filenames_to_exclude)
        and (
            (f.split(".")[-1] in extensions_to_collect)
            or any(path in f for path in filenames_to_include)
        )
    ]
    return [p.replace("\\", "/") for p in response]


def parse(paths: list) -> dict:
    tree = defaultdict(list)
    for path in paths:
        tree["/".join(path.split("/")[:-1]).replace("./", "")].append(
            path.replace("./", "")
        )
    return dict(tree)


def collect(path: str) -> None:
    artifacts = f"{target_dir}/{path.replace('./', '').split('/')[0]}"
    if os.path.isdir(artifacts):
        shutil.rmtree(artifacts)
    tree = parse(walk(path))
    for path, files in tree.items():
        os.makedirs(f"{target_dir}/{path}")
        for f in files:
            with open(f"{target_dir}/{f}.md", "w") as buffer:
                filename = f.split("/")[-1]
                ext = filename.split(".")[-1]
                buffer.writelines(
                    [
                        "---\n",
                        "search:\n",
                        "   exclude: true\n",
                        "---\n",
                        "\n",
                        f"# `{filename}`\n",
                        "\n",
                        f'!!! abstract "Source"\n'
                        f'    ```{ext} title="{filename}" linenums="1"\n',
                        f'    --8<-- "./{f}"\n',
                        "    ```\n",
                    ]
                )


if __name__ == "__main__":
    source_code_path: str = ...
    collect(source_code_path)
```

At the end of the day, it boils down to:

1. traverse the source code starting from the given `source_code_path`;
2. replicate the source code folders tree in the `target_dir` docs subfolder;
3. embed each raw source code file in a generated markdown with the [`--8<--` notation](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#embedding-external-files).

Some additional tricks are highlighted in the snippet:

- at line 52, the generated markdown is excluded from the scope of the search plugin;
- at line 57, the collected source code is wrapped into an admonition;
- at line 58, the extension of the collected source code file is used for syntax highlighting.

[^1]: For example, the codebase should be available as a proper Python package in the docs build environment for docstrings collection purposes.
