from dataclasses import dataclass

from generated.place_lighting_version_structure import (
    PlaceLightingVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceLighting(PlaceLightingVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for LIGHTING EQUIPMENT (e.g. lamp post).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
