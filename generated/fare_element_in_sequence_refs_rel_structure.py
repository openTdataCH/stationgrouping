from dataclasses import dataclass, field
from typing import List, Union

from generated.access_right_in_product_ref import AccessRightInProductRef
from generated.controllable_element_in_sequence_ref import (
    ControllableElementInSequenceRef,
)
from generated.fare_structure_element_in_sequence_ref import (
    FareStructureElementInSequenceRef,
)
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareElementInSequenceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a  FARE STRUCTURE ELEMENT IN
    SEQUENCE.
    """

    class Meta:
        name = "fareElementInSequenceRefs_RelStructure"

    controllable_element_in_sequence_ref_or_fare_structure_element_in_sequence_ref_or_access_right_in_product_ref: List[
        Union[
            ControllableElementInSequenceRef,
            FareStructureElementInSequenceRef,
            AccessRightInProductRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequenceRef",
                    "type": FareStructureElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
