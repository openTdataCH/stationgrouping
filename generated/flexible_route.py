from dataclasses import dataclass

from generated.flexible_route_version_structure import (
    FlexibleRouteVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleRoute(FlexibleRouteVersionStructure):
    """Specialisation of ROUTE for flexible service.

    May include both point and zonal areas and ordered and unordered
    sections.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
