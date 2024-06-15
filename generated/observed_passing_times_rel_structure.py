from dataclasses import dataclass, field
from typing import List

from generated.observed_passing_time import ObservedPassingTime
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObservedPassingTimesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of OBSERVED PASSING TIME.
    """

    class Meta:
        name = "observedPassingTimes_RelStructure"

    observed_passing_time: List[ObservedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "ObservedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
