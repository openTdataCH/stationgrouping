from dataclasses import dataclass

from generated.fare_element_in_sequence_versioned_child_structure import (
    FareElementInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareElementInSequence(FareElementInSequenceVersionedChildStructure):
    """
    A FARE STRUCTURE ELEMENT as a part of a VALIDABLE ELEMENT, including its
    possible order in the sequence of FARE STRUCTURE ELEMENTs forming that
    VALIDABLE ELEMENT, and its possible quantitative limitation.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
