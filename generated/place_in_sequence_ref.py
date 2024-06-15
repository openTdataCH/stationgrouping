from dataclasses import dataclass

from generated.place_in_sequence_ref_structure import (
    PlaceInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceInSequenceRef(PlaceInSequenceRefStructure):
    """Reference to a PLACE IN SEQUENCE.

    If given by context does not need to be stated.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
