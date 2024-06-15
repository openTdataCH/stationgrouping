from dataclasses import dataclass

from generated.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutePointRefStructure(PointRefStructure):
    """
    Type for a reference to a ROUTE POINT.
    """
