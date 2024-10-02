# Snippets

## Jupyter

### autoreload

```python
%load_ext autoreload
%autoreload 2
```

### profiling

```python
%load_ext line_profiler

def function_to_profile(arg: int):
    ...

%lprun -f function_to_profile function_to_profile(1)
```

For reference see [here](https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html) and [here](https://ipython-books.github.io/43-profiling-your-code-line-by-line-with-line_profiler/).

## sklearn

### `TimeSeriesSplitMultiStep`

```python
import numpy as np
import pandas as pd
from sklearn import model_selection


def TimeSeriesSplitMultiStep(series: pd.DataFrame, 
                             n_splits: int = 3, 
                             n_steps: int = 3, 
                             max_train_size: Optional[int] = None) -> tuple:
    """Extend sklearn' TimeSeriesSplit to the multistep case.

    Args:
        series (pd.DataFrame): input time series.
        n_splits (optional, int): number of splits. Defaults to 3.
        n_steps (optional, int): number of steps ahead. Defaults to 3.
        max_train_size (optional, Optional[int]): maximum training set size. Defaults to None.

    Returns:
        Indices for splitting.
    """
    tscv = model_selection.TimeSeriesSplit(n_splits, max_train_size)

    for train_index, test_index in tscv.split(series):
        last_test_index = test_index[-1]
        step_to_add = n_steps - len(test_index)
        if last_test_index < len(series) - step_to_add:
            if step_to_add > 0:
                for next_step in range(last_test_index + 1, step_to_add + last_test_index + 1):
                    test_index = np.append(test_index, next_step)
            yield train_index, test_index
```

## stdlib

### `clean_text`

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

### dbc

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

### `flatten`

```python
import numpy as np
import pandas as pd


def flatten(x: list | pd.Series | np.ndarray | tuple | map) -> list:
    """Flatten nested input list.

    Credits to [Samuele Fiorini](https://github.com/samuelefiorini).

    Args:
        x (list): nested list

    Returns:
        Flattened list.
    """
    return (
        [xi for l in x for xi in flatten(l)] if isinstance(x, (list, np.ndarray, tuple)) 
        else flatten(list(x)) if isinstance(x, (pd.Series, map))
        else [x]
    )

x = [[1, 2, 3], 4, [5], [6, 7]]
print(flatten(x)) # [1, 2, 3, 4, 5, 6, 7]
```

### `groupby`

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

### `make_deps_graph`

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

### `make_project_tree`

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

### `mround`

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

### `print`

This solution depends on `python-dotenv`, `loguru` and `icecream`: with the following setup in the root `__init__.py` of a given (managed) library, the standard `print` is overridden with a combo between a [Loguru](https://github.com/Delgan/loguru) sink with DEBUG level and the useful features provided by [IceCream](https://github.com/gruns/icecream).

!!! warning

    This comes at a price: overriding the standard `print` actually breaks Jupyter debugging features in VSC, as stated in [this issue](https://github.com/microsoft/vscode-jupyter/issues/11546).

=== " __init__.py "

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

The above setup also prevents from dangling `ic()` calls accidentally left into production code, without the need of [verbose try-except](https://github.com/gruns/icecream#import-tricks).

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

### `timed`

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

### `validate_type_annotations`

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

## streamlit

### `AgGrid`

#### Deferred single row deletion

Originally posted at [discuss.streamlit.io](https://discuss.streamlit.io/t/ag-grid-component-with-input-support/8108/167).

```python
import string

import numpy as np
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

st.set_page_config(layout='wide')


def display_table(df: pd.DataFrame) -> AgGrid:
    # Configure AgGrid options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection('single')
    st.write(f"Dataframe shape: {df.shape}")
    return AgGrid(
        df,
        gridOptions=gb.build(),
        # this override the default VALUE_CHANGED
        update_mode=GridUpdateMode.MODEL_CHANGED
    )


## Define dummy data
rng = np.random.default_rng(2021)
N_SAMPLES = 100
N_FEATURES = 10
df = pd.DataFrame(rng.integers(0, N_SAMPLES, size=(
    N_SAMPLES, N_FEATURES)), columns=list(string.ascii_uppercase[:N_FEATURES]))

cols = st.columns(2)

with cols[0]:

    st.markdown('# 🠔 Before')

    # Display AgGrid from data and write response
    st.markdown("### 1️⃣ Let's display dummy data through AgGrid")
    response = display_table(df)

    st.markdown(
        "### 2️⃣ AgGrid response contains `data` (original df) and `selected_rows`")
    for k, v in response.items():
        st.write(k, v)

with cols[1]:

    st.markdown('# 🠖 After')

    # Retrieve selected rows indices
    st.markdown(
        "### 3️⃣ From selected rows we can obtain dataframe indices to drop")
    data = response['data'].to_dict(orient='records')
    indices = [data.index(row) for row in response['selected_rows']]
    st.write(f"Selected rows are located at indices: {indices}")

    # Use retrieved indices to remove corresponding rows from dataframe
    st.markdown(
        "### 4️⃣ Display the updated dataframe where rows have been removed")
    _df = df.drop(indices, axis=0)
    st.write(f"Dataframe shape: {_df.shape}")
    AgGrid(_df)
```

#### Realtime single row deletion

Originally posted at [discuss.streamlit.io](https://discuss.streamlit.io/t/ag-grid-component-with-input-support/8108/171).

```python
import string

import numpy as np
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode

st.set_page_config(layout='wide')


def display_table(df: pd.DataFrame) -> AgGrid:
    # Configure AgGrid options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection('single', use_checkbox=True)
    
    # Custom JS code for interactive rows deletion
    # For credits SEE: 
    # https://github.com/PablocFonseca/streamlit-aggrid/blob/1acb526ba43b5aac9c8eb22cc54eeb05696cd84d/examples/example_highlight_change.py#L21
    # https://ag-grid.zendesk.com/hc/en-us/articles/360020160932-Removing-selected-rows-or-cells-when-Backspace-or-Delete-is-pressed
    js = JsCode("""
    function(e) {
        let api = e.api;        
        let sel = api.getSelectedRows();
        
        api.applyTransaction({remove: sel});
    };
    """)
    gb.configure_grid_options(onRowSelected=js) 
    return AgGrid(
        df,
        gridOptions=gb.build(),
        # this override the default VALUE_CHANGED
        update_mode=GridUpdateMode.MODEL_CHANGED,
        # needed for js injection
        allow_unsafe_jscode=True
    )


## Define dummy data
rng = np.random.default_rng(2021)
N_SAMPLES = 100
N_FEATURES = 10
df = pd.DataFrame(rng.integers(0, N_SAMPLES, size=(
    N_SAMPLES, N_FEATURES)), columns=list(string.ascii_uppercase[:N_FEATURES]))

st.info("Select a row to remove it")
response = display_table(df)
st.write(f"Dataframe shape: {response['data'].shape}")
```

#### Deferred multiple rows deletion

Originally posted at [discuss.streamlit.io](https://discuss.streamlit.io/t/ag-grid-component-with-input-support/8108/216).

```python
import string

import numpy as np
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

st.set_page_config(layout='wide')

def display_table(df: pd.DataFrame) -> AgGrid:
    # Configure AgGrid options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection('multiple', use_checkbox=True) 
    return AgGrid(
        df,
        gridOptions=gb.build(),
        # this override the default VALUE_CHANGED
        update_mode=GridUpdateMode.MODEL_CHANGED
    )


## Define dummy data
rng = np.random.default_rng(2021)
N_SAMPLES = 100
N_FEATURES = 10
df = pd.DataFrame(rng.integers(0, N_SAMPLES, size=(
    N_SAMPLES, N_FEATURES)), columns=list(string.ascii_uppercase[:N_FEATURES]))

## Display data and selected rows
left, right = st.columns(2)
with left:
    st.info("Select rows to be deleted")
    response = display_table(df)
with right:
    st.warning("Rows selected for deletion")
    rows_to_delete = pd.DataFrame(response['selected_rows'])
    st.write(rows_to_delete)

## Delete rows on button press
if st.button("Delete rows") and not rows_to_delete.empty:
    # Lookup table is needed because AgGrid does not return rows indices
    lookup = df.merge(rows_to_delete, on=list(df.columns), how='left', indicator=True)
    _df = df.drop(lookup[lookup['_merge'] == 'both'].index)
    st.success('Rows deleted')
    st.write(_df)
```

### `folium_map`

```python
import folium
import streamlit as st
from streamlit_folium import folium_static


def folium_map(geomap: folium.Map, height: int = 800) -> None:
    """Render a responsive Folium map via streamlit-folium component.

    Args:
        geomap (folium.Map): Geo map.
        height (optional, int): map height. Defaults to 800.
    """
    make_map_responsive = """
    <style>
    [title~="st.iframe"] { width: 100%}
    </style>
    """
    st.markdown(make_map_responsive, unsafe_allow_html=True)
    folium_static(geomap, height=height)
```

### `folium_dual_map`

```python
from folium import plugins
import streamlit as st
import streamlit.components.v1 as st_components


def folium_dual_map(dualmap: plugins.DualMap, height: int = 800) -> None:
    """Render a responsive Folium DualMap via streamlit-folium component.

    Args:
        dualmap (plugins.DualMap): dual geo map.
        height (optional, int): map height. Defaults to 800.
    """
    make_map_responsive = """
    <style>
    [title~="st.iframe"] { width: 100%}
    </style>
    """
    st.markdown(make_map_responsive, unsafe_allow_html=True)
    st_components.html(
        dualmap._repr_html_(),
        height=height
    )
```

### Grid layout

```python
from typing import Callable, ContextManager
import streamlit as st

def make_grid(n_rows: int, n_cols: int) -> Callable:
    """Build a grid context manager.

    Inspired from https://towardsdatascience.com/how-to-create-a-grid-layout-in-streamlit-7aff16b94508.

    Args:
        n_rows (int): number of rows.
        n_cols (int): number of cols.

    Returns:
        Callable context manager.
    """
    grid = [st.columns(n_rows) for _ in range(n_cols)]
    def _grid(i: int, j: int) -> ContextManager:
        return grid[i][j]
    return _grid

grid = make_grid(2, 2)

for i in range(2):
    for j in range(2):
        with grid(i, j):
            st.markdown(f'# Hello from ({i}, {j})')
```

### Injecting `javascript`

```python
import streamlit.components.v1 as components

## SEE: 
## - https://github.com/streamlit/streamlit/issues/1291#issuecomment-1022408379
## - https://discuss.streamlit.io/t/injecting-js/22651
## - https://www.w3schools.com/jsref/event_onclick.asp
components.html('''
    <h3 id="demo" onclick="myFunction()">Click me to change my color.</h3>

    <script>
    function myFunction() {
        let color = document.getElementById("demo").style.color;
        if (color != "red") {
            document.getElementById("demo").style.color = "red";
            }
        else {
            document.getElementById("demo").style.color = "black";
            }
    }
    </script>
    '''
) 
```

### `loguru_to_streamlit`

```python
import streamlit as st
from loguru import logger


def redirect_loguru_to_streamlit() -> None:
    """Redirect Loguru logs to Streamlit."""
    def _filter_warning(record):
        return record["level"].no == logger.level("WARNING").no    
    if 'warning_logger' not in st.session_state:
        st.session_state['warning_logger'] = logger.add(st.warning, 
                                                        filter=_filter_warning, 
                                                        level='INFO')
    if 'error_logger' not in st.session_state:
        st.session_state['error_logger'] = logger.add(st.error, level='ERROR')
```

