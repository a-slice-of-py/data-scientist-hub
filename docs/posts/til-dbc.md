---
date: 2024-10-02
authors:
  - silvio
categories:
  - TIL
tags:
  - Python
---

# Design by contract programming

Today, thanks to [PyCoder's Weekly](https://pycoders.com/issues), I discovered [this blog post](https://colorsofcode.ghost.io/counting-sheeps-with-contracts-in-python/) and more generally learned about [design by contract (DbC)](https://en.wikipedia.org/wiki/Design_by_contract) methodology.

Inspired from it, I decided to write down a simple snippet to implement _preconditions_ and _postconditions_ through Python decorators.

<!-- more -->

The final snippet, available also [here](/data-scientist-hub/resources/snippets/#dbc), is heavily inspired from [this old answer on Stack Overflow](https://stackoverflow.com/a/12151531) and the [source code](https://gitlab.com/leogermond/python-dbc/-/blob/main/dbc.py?ref_type=heads) linked to the previous blog post:

```python
import functools
from typing import Callable


def condition(
    pre: bool,
    check: Callable | None = None,
    message: str | None = None,
    placeholder: str = "abort",
):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if check is not None:
                if pre and not check(*args, **kwargs):
                    raise ValueError(
                        f"Precondition not satisfied: {message or placeholder}"
                    )
                response = func(*args, **kwargs)
                if not pre and not check(response):
                    raise ValueError(
                        f"Postcondition not satisfied: {message or placeholder}"
                    )
                return response

        return wrapper

    return decorator


def precondition(check: Callable, description: str | None = None):
    return condition(pre=True, check=check, message=description)


def postcondition(check: Callable, description: str | None = None):
    return condition(pre=False, check=check, message=description)
```

## Example

A very toy example of the usage:

```python
@precondition(lambda x: x > 0, description="Input must be positive.")
@precondition(lambda x: x % 2 == 0, description="Input must be even.")
@postcondition(lambda x: x > 4, description="Output must be > 4.")
def test(x: int) -> int:
    return 2*x

>>> test(-1) # ValueError: Precondition not satisfied: Input must be positive.
>>> test(1)  # ValueError: Precondition not satisfied: Input must be even.
>>> test(2)  # ValueError: Postcondition not satisfied: Output must be > 4.
>>> test(4)  # 8
```
