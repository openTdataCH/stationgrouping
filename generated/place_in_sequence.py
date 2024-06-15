from dataclasses import dataclass

from generated.place_in_sequence_versioned_child_structure import (
    PlaceInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceInSequence(PlaceInSequenceVersionedChildStructure):
    """Point traversed by  a NAVIGATION PATH  in sequence.

    May be a PLACE PATH JUNCTION or POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
