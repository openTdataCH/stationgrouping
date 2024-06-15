from dataclasses import dataclass, field
from typing import Optional

from generated.fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from generated.time_unit_ref import TimeUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a TIME UNIT PRICEs.
    """

    class Meta:
        name = "TimeUnitPrice_VersionedChildStructure"

    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
