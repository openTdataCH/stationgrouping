from dataclasses import dataclass, field
from typing import List, Union

from generated.controllable_element import ControllableElement
from generated.controllable_element_ref import ControllableElementRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CONTROLLABLE ELEMENT PRICEs.
    """

    class Meta:
        name = "controllableElements_RelStructure"

    controllable_element_ref_or_controllable_element: List[
        Union[ControllableElementRef, ControllableElement]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementRef",
                    "type": ControllableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElement",
                    "type": ControllableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
