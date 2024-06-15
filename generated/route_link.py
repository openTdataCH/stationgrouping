from dataclasses import dataclass

from generated.route_link_version_structure import RouteLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteLink(RouteLinkVersionStructure):
    """An oriented link between two ROUTE POINTs allowing the definition of a
    unique path through the network.

    Because ROUTE LINKs are directional   there will be separate links
    for each direction of a route.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
