from dataclasses import dataclass, field
from typing import List, Union

from generated.journey_pattern_run_time import JourneyPatternRunTime
from generated.journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternRunTimesRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of JOURNEY PATTERN RUN TIMEs.
    """

    class Meta:
        name = "journeyPatternRunTimes_RelStructure"

    journey_pattern_run_time_ref_or_journey_pattern_run_time: List[
        Union[JourneyPatternRunTimeRef, JourneyPatternRunTime]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPatternRunTimeRef",
                    "type": JourneyPatternRunTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRunTime",
                    "type": JourneyPatternRunTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
