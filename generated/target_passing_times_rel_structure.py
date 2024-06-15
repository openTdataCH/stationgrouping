from dataclasses import dataclass, field
from typing import List

from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.target_passing_time import TargetPassingTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TargetPassingTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of TARGET PASSING TIME.
    """

    class Meta:
        name = "targetPassingTimes_RelStructure"

    target_passing_time: List[TargetPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "TargetPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
