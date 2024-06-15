from dataclasses import dataclass

from generated.road_link_ref_by_value_structure import (
    RoadLinkRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadLinkRefByValue(RoadLinkRefByValueStructure):
    """
    Reference to a ROAD LINK BY VALUE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
