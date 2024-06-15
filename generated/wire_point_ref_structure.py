from dataclasses import dataclass

from generated.infrastructure_point_ref_structure import (
    InfrastructurePointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WirePointRefStructure(InfrastructurePointRefStructure):
    """
    Type for Reference to a WIRE POINT.
    """
