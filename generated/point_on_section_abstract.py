from dataclasses import dataclass

from generated.point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnSectionAbstract(PointInLinkSequenceVersionedChildStructure):
    """DUmmy Supertype for Point On SECTION.

    +v1.1.
    """

    class Meta:
        name = "PointOnSection_"
        namespace = "http://www.netex.org.uk/netex"
