# streamlit

## `AgGrid`

### Deferred single row deletion

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


# Define dummy data
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

### Realtime single row deletion

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


# Define dummy data
rng = np.random.default_rng(2021)
N_SAMPLES = 100
N_FEATURES = 10
df = pd.DataFrame(rng.integers(0, N_SAMPLES, size=(
    N_SAMPLES, N_FEATURES)), columns=list(string.ascii_uppercase[:N_FEATURES]))

st.info("Select a row to remove it")
response = display_table(df)
st.write(f"Dataframe shape: {response['data'].shape}")
```

### Deferred multiple rows deletion

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


# Define dummy data
rng = np.random.default_rng(2021)
N_SAMPLES = 100
N_FEATURES = 10
df = pd.DataFrame(rng.integers(0, N_SAMPLES, size=(
    N_SAMPLES, N_FEATURES)), columns=list(string.ascii_uppercase[:N_FEATURES]))

# Display data and selected rows
left, right = st.columns(2)
with left:
    st.info("Select rows to be deleted")
    response = display_table(df)
with right:
    st.warning("Rows selected for deletion")
    rows_to_delete = pd.DataFrame(response['selected_rows'])
    st.write(rows_to_delete)

# Delete rows on button press
if st.button("Delete rows") and not rows_to_delete.empty:
    # Lookup table is needed because AgGrid does not return rows indices
    lookup = df.merge(rows_to_delete, on=list(df.columns), how='left', indicator=True)
    _df = df.drop(lookup[lookup['_merge'] == 'both'].index)
    st.success('Rows deleted')
    st.write(_df)
```

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
