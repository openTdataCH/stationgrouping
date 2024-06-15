from dataclasses import dataclass

from generated.link_version_structure import LinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLink2(LinkVersionStructure):
    """
    A Dummy Supertype for Infrastructure Link Types.
    """

    class Meta:
        name = "InfrastructureLink_"
        namespace = "http://www.netex.org.uk/netex"
