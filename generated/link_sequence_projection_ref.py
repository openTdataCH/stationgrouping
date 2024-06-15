from dataclasses import dataclass

from generated.link_sequence_projection_ref_structure import (
    LinkSequenceProjectionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkSequenceProjectionRef(LinkSequenceProjectionRefStructure):
    """
    Reference to a LINK SEQUENCE PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
