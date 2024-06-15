from dataclasses import dataclass, field
from typing import List

from generated.place_in_sequence import PlaceInSequence
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlacesInSequenceRelStructure(StrictContainmentAggregationStructure):
    """
    A collection of one or more PLACEs in SEQUENCE.
    """

    class Meta:
        name = "placesInSequence_RelStructure"

    place_in_sequence: List[PlaceInSequence] = field(
        default_factory=list,
        metadata={
            "name": "PlaceInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
