from dataclasses import dataclass

from generated.route_ref_structure import RouteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteRef(RouteRefStructure):
    """
    Reference to a ROUTE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
