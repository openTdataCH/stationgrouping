from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.dead_run_journey_pattern import DeadRunJourneyPattern
from generated.journey_pattern_view import JourneyPatternView
from generated.sections_in_sequence_rel_structure import JourneyPattern
from generated.service_journey_pattern import ServiceJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of JOURNEY PATTERNs.
    """

    class Meta:
        name = "journeyPatternsInFrame_RelStructure"

    choice: List[
        Union[
            ServiceJourneyPattern,
            DeadRunJourneyPattern,
            JourneyPattern,
            JourneyPatternView,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPattern",
                    "type": ServiceJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPattern",
                    "type": DeadRunJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern",
                    "type": JourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternView",
                    "type": JourneyPatternView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
