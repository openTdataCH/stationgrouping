from dataclasses import dataclass

from generated.fare_element_in_sequence_ref_structure import (
    FareElementInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementInSequenceRefStructure(
    FareElementInSequenceRefStructure
):
    """
    Type for Reference to a FARE STRUCTURE ELEMENT IN SEQUENCE.
    """
