---
date: 2024-01-03
authors:
  - silvio
categories:
  - TIL
tags:
  - Python
---

# Terminal User Interface

If you have an already up-and-running [Typer app](https://github.com/tiangolo/typer), you might want to extend it to some sort of GUI _(Graphical User Interface)_.

While building a full GUI can be time-consuming, there is a really fast utility which can be adopted to get somewhere in between.

<!-- more -->

We can indeed take advantage of [Click](https://github.com/pallets/click/), the command line interfaces builder underlying Typer itself. Since the former has been eagerly adopted almost anywhere a CLI is required, it represents a leader in the Python ecosystem.

Given so, other libraries have built on-top of Click as Typer did: one of them is [Trogon](https://github.com/Textualize/trogon), which basically provides TUI _(Terminal User Interface)_ based on [Textual](https://github.com/textualize/textual) around Click apps.

As pointed out in [this thread](https://github.com/Textualize/trogon/issues/10), Trogon can therefore do his job also on Typer apps:

```python
import typer
from trogon import Trogon
from typer.main import get_group

app = typer.Typer()

# ... pre-existing Typer app

@app.command()
def launch_tui(ctx: typer.Context):
    Trogon(get_group(app), click_context=ctx).run()
```

This is a nice add-on for Typer apps, which still remain completely available: Trogon's TUI just corresponds to a brand new command in a Typer app i.e., `launch-tui` in the above example.
