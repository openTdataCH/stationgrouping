from dataclasses import dataclass

from generated.fare_element_in_sequence_ref_structure import (
    FareElementInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareElementInSequenceRef(FareElementInSequenceRefStructure):
    """
    Reference to a FARE ELEMENT IN SEQUENCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
