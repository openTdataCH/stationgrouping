from dataclasses import dataclass, field
from typing import List

from generated.destination_display_variant import DestinationDisplayVariant
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariantsRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of DESTINATION DISPLAY VARIANTs.
    """

    class Meta:
        name = "destinationDisplayVariants_RelStructure"

    destination_display_variant: List[DestinationDisplayVariant] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
