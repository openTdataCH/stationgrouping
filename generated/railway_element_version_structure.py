from dataclasses import dataclass, field

from generated.infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)
from generated.railway_point_ref_structure import RailwayPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayElementVersionStructure(InfrastructureLinkVersionStructure):
    """
    Type for RAILWAY ELEMENT.

    :ivar from_point_ref: Identifier of POINT from which Link starts.
    :ivar to_point_ref: Identifier of POINT at which Link ends.
    """

    class Meta:
        name = "RailwayElement_VersionStructure"

    from_point_ref: RailwayPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: RailwayPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
