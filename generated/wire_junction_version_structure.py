from dataclasses import dataclass

from generated.infrastructure_point_version_structure import (
    InfrastructurePointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireJunctionVersionStructure(InfrastructurePointVersionStructure):
    """
    Type for WIRE JUNCTION.
    """

    class Meta:
        name = "WireJunction_VersionStructure"
