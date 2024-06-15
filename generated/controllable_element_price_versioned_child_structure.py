from dataclasses import dataclass, field
from typing import Optional

from generated.controllable_element_ref import ControllableElementRef
from generated.fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    """
    Type for a CONTROLLABLE ELEMENT PRICE.
    """

    class Meta:
        name = "ControllableElementPrice_VersionedChildStructure"

    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
