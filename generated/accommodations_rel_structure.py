from dataclasses import dataclass, field
from typing import List, Union

from generated.accommodation import Accommodation
from generated.accommodation_ref import AccommodationRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationsRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SERVICE FACILITY SETs.
    """

    class Meta:
        name = "accommodations_RelStructure"

    accommodation_ref_or_accommodation: List[
        Union[AccommodationRef, Accommodation]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccommodationRef",
                    "type": AccommodationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Accommodation",
                    "type": Accommodation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
