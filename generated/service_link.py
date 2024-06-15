from dataclasses import dataclass

from generated.service_link_version_structure import (
    ServiceLinkVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLink(ServiceLinkVersionStructure):
    """A LINK between an ordered pair of STOP POINTs.

    Service links are directional - there will be separate links for each direction of a route.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
