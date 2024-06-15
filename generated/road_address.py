from dataclasses import dataclass

from generated.road_address_version_structure import (
    RoadAddressVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadAddress(RoadAddressVersionStructure):
    """
    Specialisation of ADDRESS refining it by using the characteristics such as road
    number, and name used for conventional identification of along a road.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
