from dataclasses import dataclass

from generated.fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FarePrice1(FarePriceVersionedChildStructure):
    """
    A set of all possible price features for a Fare element.
    """

    class Meta:
        name = "FarePrice"
        namespace = "http://www.netex.org.uk/netex"
