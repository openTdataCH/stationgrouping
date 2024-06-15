from dataclasses import dataclass

from generated.route_derived_view_structure import RouteDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteView(RouteDerivedViewStructure):
    """
    Annotated reference to a ROUTE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
