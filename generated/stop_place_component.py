from dataclasses import dataclass

from generated.stop_place_component_version_structure import (
    StopPlaceComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceComponent(StopPlaceComponentVersionStructure):
    """
    An element of a STOP PLACE describing part of its structure.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
