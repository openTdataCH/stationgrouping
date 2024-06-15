from dataclasses import dataclass

from generated.road_point_ref_structure import RoadPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadPointRef(RoadPointRefStructure):
    """
    Reference to a ROAD POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
