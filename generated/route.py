from dataclasses import dataclass

from generated.route_version_structure import RouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Route(RouteVersionStructure):
    """An ordered list of located POINTs defining one single path through the Road
    (or rail) network.

    A ROUTE may pass through the same POINT more than once.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
