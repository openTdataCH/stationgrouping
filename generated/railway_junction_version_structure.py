from dataclasses import dataclass

from generated.infrastructure_point_version_structure import (
    InfrastructurePointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayJunctionVersionStructure(InfrastructurePointVersionStructure):
    """
    Type for RAILWAY JUNCTION.
    """

    class Meta:
        name = "RailwayJunction_VersionStructure"
