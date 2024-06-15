from dataclasses import dataclass, field
from typing import List, Union

from generated.empty_type_2 import EmptyType2
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.via_versioned_child_structure import ViaVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ViasRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of VIA Names.
    """

    class Meta:
        name = "vias_RelStructure"

    none_or_via: List[Union[EmptyType2, ViaVersionedChildStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "None",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Via",
                    "type": ViaVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
