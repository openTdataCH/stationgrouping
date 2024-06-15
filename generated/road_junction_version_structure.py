from dataclasses import dataclass

from generated.infrastructure_point_version_structure import (
    InfrastructurePointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadJunctionVersionStructure(InfrastructurePointVersionStructure):
    """
    Type for ROAD JUNCTION.
    """

    class Meta:
        name = "RoadJunction_VersionStructure"
