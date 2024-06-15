from dataclasses import dataclass, field

from generated.infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)
from generated.road_point_ref_structure import RoadPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadElementVersionStructure(InfrastructureLinkVersionStructure):
    """
    Type for ROAD ELEMENT.

    :ivar from_point_ref: Identifier of POINT from which Link starts.
    :ivar to_point_ref: Identifier of POINT at which Link ends.
    """

    class Meta:
        name = "RoadElement_VersionStructure"

    from_point_ref: RoadPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: RoadPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
