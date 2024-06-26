from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.journey_meeting import JourneyMeeting

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  JOURNEY MEETINGs.
    """

    class Meta:
        name = "journeyMeetingsInFrame_RelStructure"

    journey_meeting: List[JourneyMeeting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyMeeting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
