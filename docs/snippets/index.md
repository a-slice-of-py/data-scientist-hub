# Snippets

The temple of [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself): collection of snippets of reusable code.

<figure>
    <img src="https://imgs.xkcd.com/comics/is_it_worth_the_time.png"
         title="Is it worth the time? by XKCD"
         alt="Is it worth the time? by XKCD">
    <figcaption><small>
    credits to: <a href="https://imgs.xkcd.com/comics/is_it_worth_the_time.png">XKCD</a>
    </small></figcaption>
</figure>

## Python

??? tip "Try here!"
    <iframe
    src="https://www.programiz.com/python-programming/online-compiler/"
    title="Programiz Python terminal"
    width="100%"
    height="500"
    scrolling="no">
    </iframe>

### boto3

#### `put_log_events`

```python
from datetime import datetime

import boto3
from loguru import logger

session = boto3.session.Session(profile_name=..., region_name=...)
client = session.client('logs')
LOG_GROUP_NAME = ...


def _create_log_stream(log_stream_name: str) -> None:
    """Create log stream if not exists already.

    Args:
        log_stream_name (str): log stream name.
    """
    try:
        _ = client.create_log_stream(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name
        )
        logger.info(f'Log stream {log_stream_name} created.')
    except client.exceptions.ResourceAlreadyExistsException:
        logger.info(f'Log stream {log_stream_name} already exists.')


def _put_log_events(log_stream_name: str, log_events: list) -> dict:
    """Put log events on the given log stream.

    Args:
        log_stream_name (str): target log stream name.
        log_events (list): list of strings (events message to log).

    Returns:
        Put operation response.
    """
    # Log events must be in the form {'timestamp': ..., 'message': ...}.
    now = int(datetime.now().timestamp() * 1000)
    _log_events = list(
        map(lambda x: {'timestamp': now, 'message': str(x)}, log_events))
    try:
        response = client.put_log_events(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name,
            logEvents=_log_events
        )
        logger.info(f'First log submitted to log stream {log_stream_name}')
    except client.exceptions.InvalidSequenceTokenException as e:
        # Parse exception to retrieve expected sequence token
        sequence_token = str(str(e).split(': ')[-1])
        response = client.put_log_events(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name,
            logEvents=_log_events,
            sequenceToken=sequence_token
        )
    logger.info(f'Events successfully logged to log stream {log_stream_name}.')
    return response


def put_log_events(log_stream_name: str, log_events: list) -> dict:
    """Put log events on the given log stream.

    This function wraps also the (possible) creation of the log stream beforehand.

    Args:
        log_stream_name (str): target log stream name.
        log_events (list): list of strings (events message to log).

    Returns:
        Put operation response.
    """
    _create_log_stream(log_stream_name)
    return _put_log_events(log_stream_name, log_events)
```

### folium

#### `cartographer`

```python
"""Base Cartographer interface."""

from collections import OrderedDict
from typing import Optional

import folium
from folium import plugins
from loguru import logger


class BaseCartographer:
    """Implement a base class handle Folium map."""

    def __init__(self, map_location: Optional[tuple] = None) -> None:
        """Init map."""
        self.map_location = map_location
        self.reset_map()

    def _set_map(self) -> None:
        """Set base map."""
        if self.map_location:
            self.map = folium.Map(
                location=self.map_location,
                tiles=None,
                zoom_start=16,
                max_zoom=19,
                control_scale=True
            )
        else:
            self.map = None
            logger.warning("No map available with map_location = None.")

    def _set_map_tiles(self) -> None:
        """Set map tiles."""
        self.tiles = OrderedDict(
            openstreetmap=dict(
                tiles='openstreetmap',
                attr=None,
                name='Open Street Map',
                control=True
            ),
            esri=dict(
                tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                attr='Esri Satellite',
                name='Esri (satellite)',
                control=True
            ),
            esri_streets=dict(
                tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                attr='Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
                name='Esri (streets)',
                control=True
            ),
            stamentoner=dict(
                tiles='stamentoner',
                attr=None,
                name='Black & White',
                control=True
            ),
            cartolight=dict(
                tiles='cartodbpositron',
                attr=None,
                name='Light',
                control=True
            )
        )

    def _add_map_tiles(self) -> None:
        """Assign tiles to map."""
        self._set_map_tiles()
        for tile in self.tiles.values():
            folium.TileLayer(**tile).add_to(self.map)

    def _add_plugins(self) -> None:
        """Add plugins to map."""
        # layer control
        folium.LayerControl(collapsed=True).add_to(self.map)
        # Ruler
        self.map.add_child(plugins.MeasureControl())
        # Geocoder
        self.map.add_child(
            plugins.Geocoder(
                collapsed=True,
                position='topright',
                add_marker=True
            )
        )
        # Fullscreen
        self.map.add_child(
            plugins.Fullscreen(
                position="topleft",
                force_separate_button=False,
            )
        )
        # Draw
        self.map.add_child(
            plugins.Draw()
        )
        # Mouse position
        self.map.add_child(
            plugins.MousePosition(separator=', ')
        )

    def _make_map_layers(self) -> None:
        """Set a placeholder to fill with concrete map layers."""
        ...

    def reset_map(self) -> None:
        """Reset base map."""
        self._set_map()
        if self.map:
            self._add_map_tiles()
            self._make_map_layers()
            self._add_plugins()
```

### sklearn

#### `TimeSeriesSplitMultiStep`

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

### stdlib

#### `clean_text`

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
print(_groupby(x)) # [1, 2, 3, 2]
```

#### `mround`

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

#### `timed`

```python
import time
from datetime import timedelta
from functools import wraps
from typing import Callable, Optional

from loguru import logger


def timed(_func: Optional[Callable] = None, *, return_time: bool = False) -> Callable:
    """Print the execution time for the decorated function.

    Args:
        _func (Optional[Callable], optional): decorate function. Defaults to None.
        return_time (bool, optional): if True, returns execution time before function. Defaults to False.
    """
    def _timed(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logger.info(
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

### streamlit

#### `folium_map`

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

#### `loguru_to_streamlit`

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
