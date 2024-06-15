from dataclasses import dataclass, field
from typing import List

from generated.previous_call import PreviousCall
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PreviousCallsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for List of PREVIOUS CALLs.
    """

    class Meta:
        name = "previousCalls_RelStructure"

    previous_call: List[PreviousCall] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
