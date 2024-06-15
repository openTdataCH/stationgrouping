from dataclasses import dataclass

from generated.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructurePointRefStructure(PointRefStructure):
    """
    Type for Reference to an INFRASTRUCTURE POINT.
    """
