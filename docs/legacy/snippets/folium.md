# folium

## `BaseCartographer`

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

    def make_map(self) -> None:
        """Make map from scratch."""
        self.reset_map()
        ...

    def _on_change(self) -> None:
        """Rebuild map on each change."""
        self.make_map()
        logger.info(f"Map updated.")
```

## `DualCartographer`

```python
from ... import BaseCartographer


class DualCartographer(BaseCartographer):
    """Extend BaseCartographer to handle [Folium DualMap](https://python-visualization.github.io/folium/plugins.html#folium.plugins.DualMap)."""

    def __init__(self, s1: ..., s2: ...) -> None:
        """Initialize class.

        Args:
            s1 (...): ....
            s2 (...): ....
        """
        self._s1 = s1
        self._s2 = s2
        super().__init__(...)

    @property
    def s1(self) -> ...:
        """Set s1 as a class property.

        SEE: For reference see [here](https://stackoverflow.com/questions/19869799/catching-changes-to-a-mutable-attribute-in-python).

        Returns:
            Left map data value.
        """
        return self._s1

    @property
    def s2(self) -> ...:
        """Set s2 as a class property.

        Returns:
            Right map data value.
        """
        return self._s2

    @s1.setter
    def s1(self, value: ...) -> None:
        """Define behaviour on `s1` setattr.

        Args:
            value (...): left data.
        """
        if self._s1 != value:
            self._s1 = value
            self._on_change()

    @s2.setter
    def s2(self, value: ...) -> None:
        """Define behaviour on `s2` setattr.

        Args:
            value (...): right data.
        """
        if self._s2 != value:
            self._s2 = value
            self._on_change()

    def _set_map(self) -> None:
        """Initialize Folium DualMap."""
        self.map = plugins.DualMap(
            location=self.map_location,
            tiles=None,
            zoom_start=16,
            max_zoom=19,
            control_scale=True
        )

    def _add_map_tiles(self):
        """Assign tiles to map."""
        self._set_map_tiles()
        for tile in self.tiles.values():
            folium.TileLayer(**tile).add_to(self.map.m1)
            folium.TileLayer(**tile).add_to(self.map.m2)

    def _make_map_layers(self) -> None:
        """Define and assign layers onto map."""
        super()._make_map_layers(...)

        ...
```
