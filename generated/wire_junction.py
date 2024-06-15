from dataclasses import dataclass

from generated.wire_junction_version_structure import (
    WireJunctionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireJunction(WireJunctionVersionStructure):
    """
    A type of INFRASTRUCTURE POINT used to describe a WIRE network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
