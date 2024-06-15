from dataclasses import dataclass

from generated.infrastructure_point_ref_structure import (
    InfrastructurePointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructurePointRef(InfrastructurePointRefStructure):
    """
    Reference to an INFRASTRUCTURE POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
