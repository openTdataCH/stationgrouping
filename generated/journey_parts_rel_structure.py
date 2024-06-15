from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.journey_part import JourneyPart
from generated.journey_part_ref import JourneyPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPartsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of JOURNEY PARTs.
    """

    class Meta:
        name = "journeyParts_RelStructure"

    journey_part_ref_or_journey_part: List[
        Union[JourneyPartRef, JourneyPart]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPartRef",
                    "type": JourneyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPart",
                    "type": JourneyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
