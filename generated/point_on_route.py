from dataclasses import dataclass

from generated.point_on_route_versioned_child_structure import (
    PointOnRouteVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnRoute(PointOnRouteVersionedChildStructure):
    """
    A reference to a ROUTE POINT used to define a ROUTE with its order on that
    ROUTE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
