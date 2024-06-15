from dataclasses import dataclass, field
from typing import List, Union

from generated.point_in_journey_pattern import PointInJourneyPattern
from generated.stop_point_in_journey_pattern import StopPointInJourneyPattern
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.timing_point_in_journey_pattern import (
    TimingPointInJourneyPattern,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointsInJourneyPatternRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for POINT IN JOURNEY PATTERN.
    """

    class Meta:
        name = "pointsInJourneyPattern_RelStructure"

    point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern: List[
        Union[
            PointInJourneyPattern,
            StopPointInJourneyPattern,
            TimingPointInJourneyPattern,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointInJourneyPattern",
                    "type": PointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPattern",
                    "type": StopPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPattern",
                    "type": TimingPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 2,
        },
    )
