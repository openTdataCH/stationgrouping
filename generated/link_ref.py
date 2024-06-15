from dataclasses import dataclass

from generated.link_ref_structure import LinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkRef(LinkRefStructure):
    """
    Reference to a LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
