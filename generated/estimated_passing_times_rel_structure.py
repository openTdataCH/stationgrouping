from dataclasses import dataclass, field
from typing import List

from generated.estimated_passing_time import EstimatedPassingTime
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of ESTIMATED PASSING TIME.
    """

    class Meta:
        name = "estimatedPassingTimes_RelStructure"

    estimated_passing_time: List[EstimatedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
