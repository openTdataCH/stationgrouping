from dataclasses import dataclass, field
from typing import Optional

from generated.fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from generated.time_interval_ref import TimeIntervalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeIntervalPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    """
    Type for a TIME INTERVAL PRICEs.
    """

    class Meta:
        name = "TimeIntervalPrice_VersionedChildStructure"

    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
