from dataclasses import dataclass, field
from typing import Optional

from generated.path_links_in_sequence_rel_structure import (
    PathLinksInSequenceRelStructure,
)
from generated.place_ref_structure import PlaceRefStructure
from generated.point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceInSequenceVersionedChildStructure(
    PointInLinkSequenceVersionedChildStructure
):
    """
    Type for a PLACE in SEQUENCE.

    :ivar place_ref: Reference to a Place or Site Component , that is
        QUAY, ACCESS SPACE or BOARDING POSITION or PATH JUNCTION.
    :ivar branch_level: Branching level of place.
    :ivar onward_links: Onward links from this point.
    """

    class Meta:
        name = "PlaceInSequence_VersionedChildStructure"

    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    branch_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchLevel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onward_links: Optional[PathLinksInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "onwardLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
