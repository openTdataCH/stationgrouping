from dataclasses import dataclass

from generated.point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointInLinkSequence(PointInLinkSequenceVersionedChildStructure):
    """
    An node of an abstract LINK SEQUENCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
