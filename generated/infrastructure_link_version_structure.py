from dataclasses import dataclass

from generated.link_version_structure import LinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLinkVersionStructure(LinkVersionStructure):
    """
    Type for INFRASTRUCTURE LINK.
    """

    class Meta:
        name = "InfrastructureLink_VersionStructure"
