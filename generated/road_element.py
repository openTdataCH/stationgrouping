from dataclasses import dataclass

from generated.road_element_version_structure import (
    RoadElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadElement(RoadElementVersionStructure):
    """
    A type of INFRASTRUCTURE LINK used to describe a ROAD network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
