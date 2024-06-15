from dataclasses import dataclass, field
from typing import List, Union

from generated.cell_ref import CellRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.time_interval_price_ref import TimeIntervalPriceRef
from generated.time_interval_price_versioned_child_structure import (
    TimeIntervalPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeIntervalPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of TIME INTERVAL PRICEs.
    """

    class Meta:
        name = "timeIntervalPrices_RelStructure"

    time_interval_price_ref_or_time_interval_price_or_cell_ref: List[
        Union[
            TimeIntervalPriceRef,
            TimeIntervalPriceVersionedChildStructure,
            CellRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
