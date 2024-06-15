from dataclasses import dataclass

from generated.road_junction_version_structure import (
    RoadJunctionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadJunction(RoadJunctionVersionStructure):
    """
    A type of INFRASTRUCTURE POINT used to describe a ROAD network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
