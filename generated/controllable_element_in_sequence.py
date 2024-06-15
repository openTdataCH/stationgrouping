from dataclasses import dataclass

from generated.controllable_element_in_sequence_versioned_child_structure import (
    ControllableElementInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementInSequence(
    ControllableElementInSequenceVersionedChildStructure
):
    """
    A CONTROLLABLE ELEMENT as a part of a FARE STRUCTURE ELEMENT, including its
    possible order in the sequence of CONTROLLABLE ELEMENTs grouped together to
    form that FARE STRUCTURE ELEMENT, and its possible quantitative limitation.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
