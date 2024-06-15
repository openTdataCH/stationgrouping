from dataclasses import dataclass

from generated.link_projection_ref_structure import LinkProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkProjectionRef(LinkProjectionRefStructure):
    """
    Reference to a PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
