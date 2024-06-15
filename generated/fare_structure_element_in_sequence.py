from dataclasses import dataclass, field
from typing import Any

from generated.fare_structure_element_in_sequence_versioned_child_structure import (
    FareStructureElementInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementInSequence(
    FareStructureElementInSequenceVersionedChildStructure
):
    """
    A FARE STRUCTURE ELEMENT as a part of a VALIDABLE ELEMENT, including its
    possible order in the sequence of FARE STRUCTURE ELEMENTs forming that
    VALIDABLE ELEMENT, and its possible quantitative limitation.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
