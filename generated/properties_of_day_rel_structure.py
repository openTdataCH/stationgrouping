from dataclasses import dataclass, field
from typing import List

from generated.property_of_day import PropertyOfDay
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PropertiesOfDayRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of properties of day.
    """

    class Meta:
        name = "propertiesOfDay_RelStructure"

    property_of_day: List[PropertyOfDay] = field(
        default_factory=list,
        metadata={
            "name": "PropertyOfDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
