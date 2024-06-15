from dataclasses import dataclass, field
from typing import List

from generated.journey_headway import JourneyHeadway
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyHeadwaysRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of JOURNEY HEADWAY Interval.
    """

    class Meta:
        name = "journeyHeadways_RelStructure"

    journey_headway: List[JourneyHeadway] = field(
        default_factory=list,
        metadata={
            "name": "JourneyHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
