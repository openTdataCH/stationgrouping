from dataclasses import dataclass

from generated.point_in_sequence_ref_structure import (
    PointInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceInSequenceRefStructure(PointInSequenceRefStructure):
    """
    Type for reference to a PLACE IN SEQUENCE.
    """
