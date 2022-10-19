# stdlib

## `clean_text`

```python
from textwrap import dedent


def clean_text(x: str) -> str:
    """Remove indentation and whitespaces.

    Args:
        x (str): (possibly multiline) text.

    Returns:
        Cleaned text.
    """
    return dedent(x).strip()

x = '''
    Hi! I am
    a multiline
    text.
    '''
    
print(x)
print(clean_text(x)) # cleaner
```

## `flatten`

```python
import numpy as np
import pandas as pd


def flatten(x: list) -> list:
    """Flatten nested input list.

    Credits to [Samuele Fiorini](https://github.com/samuelefiorini).

    Args:
        x (list): nested list

    Returns:
        Flattened list.
    """
    return (
        [xi for l in x for xi in flatten(l)] if isinstance(x, (list, np.ndarray)) 
        else flatten(list(x)) if isinstance(x, (pd.Series, map))
        else [x]
    )

x = [[1, 2, 3], 4, [5], [6, 7]]
print(flatten(x)) # [1, 2, 3, 4, 5, 6, 7]
```

## `groupby`

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
print(_groupby(x)) # [1, 2, 3, 2]
```

## `make_deps_graph`

```python
import os
import subprocess


def make_deps_graph(*args, **kwargs) -> None:
    """Make dependencies graphs via pydeps."""

    # Ensure outdir exists
    outdir = ...
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    
    # Generate pydeps graph for the following paths
    fnames = [...]

    for fname in fnames:
        subprocess.run(f"pydeps {fname} --cluster --noshow -o {outdir}/{fname}.svg", shell=True)
```

## `make_project_tree`

```python
import sys
from pathlib import Path
from itertools import islice


def make_project_tree(
    out_path: Path = './project_tree.md',
    dir_path: Path = '.',
    level: int = -1,
    limit_to_directories: bool = False,
    length_limit: int = 1000,
    to_output = True,
    **kwargs
    ):
    """Save to out_path a visual tree representation of contents of a given Path object.
    
    SEE: credits to https://stackoverflow.com/a/59109706/13790005 for tree implementation.

    Args:
        out_path (Path, optional): output path. Defaults to './project_tree.md'.
        dir_path (Path, optional): path to traverse. Defaults to '.'.
        level (int, optional): depth level to traverse. Defaults to -1.
        limit_to_directories (bool, optional): whether to track only directories. Defaults to False.
        length_limit (int, optional): limit of total elements retrievable. Defaults to 1000.
        to_output (bool, optional): whether to save tree in a file. Defaults to True.
    """
    space =  '    '
    branch = '│   '
    tee =    '├── '
    last =   '└── '

    dir_path = Path(dir_path) # accept string coerceable to Path
    files = 0
    directories = 0
    blacklist = [...] # fill with path to be excluded

    def inner(
        dir_path: Path,
        prefix: str='',
        level=-1
        ) -> str:
        """Traverse folder.

        Args:
            dir_path (Path): target folder.
            prefix (str, optional): folder prefix to be added. Defaults to ''.
            level (int, optional): maximum reachable depth. Defaults to -1.

        Returns:
            Folder contents.
        """
        nonlocal files, directories
        if not level:
            return # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else:
            contents = list(filter(lambda x: all(y not in str(x) for y in blacklist), dir_path.iterdir()))
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield prefix + pointer + path.name
                directories += 1
                extension = branch if pointer == tee else space
                yield from inner(path, prefix=prefix+extension, level=level-1)
            elif not limit_to_directories:
                yield prefix + pointer + path.name
                files += 1

    if to_output:
        sys.stdout = open(out_path, "w", encoding='utf-8')
        print("# Project tree")
        print('')
        print("```")
    print(dir_path.name)
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        print(line)
    if next(iterator, None):
        print(f'... length_limit, {length_limit}, reached, counted:')
    print(f'\n{directories} directories' + (f', {files} files' if files else ''))
    if to_output:
        print("```")
        sys.stdout.close()
```

## `mround`

```python
def mround(x: float, m: int = 10) -> int:
    """Round to nearest multiple of m.

    Args:
        x (float): Value to round
        m (optional, int): desired multiple target. Defaults to 10.

    Returns:
        Rounded value.
    """
    return round(x / m) * m

x = 123.4
print(mround(x, m=10)) # 120
```

## `print`

This solution depends on `python-dotenv`, `loguru` and `icecream`: with the following setup in the root `__init__.py` of a given (managed) library, the standard `print` is overridden with a combo between a [Loguru](https://github.com/Delgan/loguru) sink with DEBUG level and useful [IceCream](https://github.com/gruns/icecream) features.

=== "__init__.py"

    ```python
    import os
    import sys

    from dotenv import load_dotenv
    from loguru import logger

    __ = load_dotenv()
    logger.remove()
    logger.add(
        sys.stdout,
        level=os.environ.get('LOGURU_LEVEL', 'DEBUG')
    )

    FROM_LOCAL = os.environ.get('FROM_LOCAL', 'false') == 'true'

    if FROM_LOCAL:
        from icecream import install, ic
        ic.configureOutput(
            prefix='',
            outputFunction=lambda x: logger.debug(x),
            includeContext=True
            )
        # SEE: this will add ic as 'print' between builtins,
        # making it available everywhere - and purposely overriding 
        # standard print()!
        install('print')
    ```

=== ".env"

    ```
    FROM_LOCAL=true
    ```

??? Example
    
    Let's define a test function:

    ```python
    def test(x: list) -> str:
        return ', '.join(map(str, x))
    ```
    
    Before, with the standard `print`:

    ```
    >>> print(test([1, 2]))
    1, 2
    ```

    After, with the new `print` obtained by importing anything from the library with the above `__init__.py`:

    ```
    >>> print(test([1, 2]))
    2022-10-19 10:20:28.588 | DEBUG | my_library:<lambda>:50 - my_script.py:1 - test([1, 2]): '1, 2'
    ```


## `timed`

```python
import time
from datetime import timedelta
from functools import wraps
from typing import Callable, Optional

from loguru import logger


def timed(_func: Optional[Callable] = None, *, return_time: bool = False) -> Callable:
    """Print the execution time for the decorated function.

    Args:
        _func (Optional[Callable], optional): function to decorate. Defaults to None.
        return_time (bool, optional): if True, returns execution time before function. Defaults to False.
    """
    def _timed(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logger.success(
                f"{func.__module__}.{func.__name__} took {str(timedelta(seconds=end - start)).split('.')[0]}.")
            if return_time:
                return end - start, result
            else:
                return result
        return wrapper
    if _func is None:
        return _timed
    else:
        return _timed(_func)
```

## `validate_type_annotations`

```python
from functools import wraps
from typing import Callable

from loguru import logger

def validate_type_annotations(func: Callable) -> Callable:
    """Validate type annotations of given function arguments enriching error messages.

    Args:
        func (Callable): function to decorate.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        func.__annotations__.pop('return', None)
        func_types = [*func.__annotations__.values()]
        input_types = list(map(lambda x: type(x), (*args, *kwargs)))
        if func_types == input_types:
            return func(*args, **kwargs)
        else:
            logger.error(
                f"Function `{func.__name__}` input types mismatch.\n Annotated: {func.__annotations__}\n Submitted: { dict(zip(func.__annotations__.keys(), input_types))}\n")
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.exception(e.__class__.__name__)
    return wrapper
```
