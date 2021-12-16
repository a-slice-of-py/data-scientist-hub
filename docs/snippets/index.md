# 🛕 Snippets

The Temple of [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself): collection of snippets of reusable code.

<figure>
    <img src="https://imgs.xkcd.com/comics/is_it_worth_the_time.png"
         title="Is it worth the time? by XKCD"
         alt="Is it worth the time? by XKCD">
    <figcaption><small>
    credits to: <a href="https://imgs.xkcd.com/comics/is_it_worth_the_time.png">XKCD</a>
    </small></figcaption>
</figure>

## Python

### Standard lib

#### `groupby`
```python
from itertools import groupby

def _groupby(x: list) -> list:
    """Groupby a list to remove consecutive duplicates while preserving ordering.

    Inspired by https://stackoverflow.com/a/5738933/13790005.

    Args:
        x (list): input list.

    Returns:
        List with removed consecutive duplicates.
    """
    return list(xi for xi, _ in groupby(x))

x = [1, 2, 2, 3, 2]
_groupby(x) # returns [1, 2, 3, 2]
```
