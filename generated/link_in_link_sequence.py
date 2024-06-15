from dataclasses import dataclass

from generated.link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkInLinkSequence(LinkInLinkSequenceVersionedChildStructure):
    """
    An edge of an abstract LINK SEQUENCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
