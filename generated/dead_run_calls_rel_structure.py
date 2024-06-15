from dataclasses import dataclass, field
from typing import List

from generated.dead_run_call_versioned_child_structure import (
    DeadRunCallVersionedChildStructure,
)
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunCallsRelStructure(StrictContainmentAggregationStructure):
    """
    DEAD RUN CALLs associated with entity.
    """

    class Meta:
        name = "deadRunCalls_RelStructure"

    dead_run_call: List[DeadRunCallVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        },
    )
