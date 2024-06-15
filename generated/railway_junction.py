from dataclasses import dataclass

from generated.railway_junction_version_structure import (
    RailwayJunctionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayJunction(RailwayJunctionVersionStructure):
    """
    A type of INFRASTRUCTURE POINT used to describe a RAILWAY network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
