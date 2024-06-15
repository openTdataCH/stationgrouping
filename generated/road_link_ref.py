from dataclasses import dataclass

from generated.road_link_ref_structure import RoadLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadLinkRef(RoadLinkRefStructure):
    """
    Reference to a ROAD LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
