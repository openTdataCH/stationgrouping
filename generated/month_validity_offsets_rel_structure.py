from dataclasses import dataclass, field
from typing import List

from generated.month_validity_offset import MonthValidityOffset
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonthValidityOffsetsRelStructure(StrictContainmentAggregationStructure):
    """
    Ser of MONTH VALIDITY OFFSETs parameters such as rounding steps for Frame.
    """

    class Meta:
        name = "monthValidityOffsets_RelStructure"

    month_validity_offset: List[MonthValidityOffset] = field(
        default_factory=list,
        metadata={
            "name": "MonthValidityOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
