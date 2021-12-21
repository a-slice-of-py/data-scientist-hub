# streamlit

## `folium_map`

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

## `folium_dual_map`

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

## `loguru_to_streamlit`

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
