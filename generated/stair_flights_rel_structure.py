from dataclasses import dataclass, field
from typing import List

from generated.stair_flight import StairFlight
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StairFlightsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FLIGHTs.

    :ivar stair_flight: FLIGHT of Stairs.
    """

    class Meta:
        name = "stairFlights_RelStructure"

    stair_flight: List[StairFlight] = field(
        default_factory=list,
        metadata={
            "name": "StairFlight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
