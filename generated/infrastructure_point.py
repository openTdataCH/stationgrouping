from dataclasses import dataclass

from generated.infrastructure_point_version_structure import (
    InfrastructurePointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructurePoint(InfrastructurePointVersionStructure):
    """
    A supertype including all POINTs of the physical network (e.g. RAILWAY
    JUNCTION).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
