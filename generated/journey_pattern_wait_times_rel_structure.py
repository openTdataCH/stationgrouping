from dataclasses import dataclass, field
from typing import List, Union

from generated.journey_pattern_wait_time import JourneyPatternWaitTime
from generated.journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternWaitTimesRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of JOURNEY PATTERN WAIT TIMEs.
    """

    class Meta:
        name = "journeyPatternWaitTimes_RelStructure"

    journey_pattern_wait_time_ref_or_journey_pattern_wait_time: List[
        Union[JourneyPatternWaitTimeRef, JourneyPatternWaitTime]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPatternWaitTimeRef",
                    "type": JourneyPatternWaitTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternWaitTime",
                    "type": JourneyPatternWaitTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
