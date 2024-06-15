from dataclasses import dataclass

from generated.link_version_structure import LinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Link(LinkVersionStructure):
    """LINK connecting two POINTs.

    An oriented spatial object of dimension 1 with view to the overall
    description of a network, describing a connection between two
    POINTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
