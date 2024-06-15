from dataclasses import dataclass

from generated.route_point_version_structure import RoutePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutePoint(RoutePointVersionStructure):
    """
    A POINT used to define the shape of a ROUTE through the network.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
