from dataclasses import dataclass, field
from typing import List

from generated.journey_layover import JourneyLayover
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyLayoversRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of JOURNEY LAYOVERs.
    """

    class Meta:
        name = "journeyLayovers_RelStructure"

    journey_layover: List[JourneyLayover] = field(
        default_factory=list,
        metadata={
            "name": "JourneyLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
