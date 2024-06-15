from dataclasses import dataclass

from generated.infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLink1(InfrastructureLinkVersionStructure):
    """A supertype including all LINKs of the physical network (e.g. RAILWAY
    ELEMENT).

    Infrastructure  links are directional - there will be separate links for each direction of a network.
    """

    class Meta:
        name = "InfrastructureLink"
        namespace = "http://www.netex.org.uk/netex"
