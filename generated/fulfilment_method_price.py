from dataclasses import dataclass

from generated.fulfilment_method_price_versioned_child_structure import (
    FulfilmentMethodPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethodPrice(FulfilmentMethodPriceVersionedChildStructure):
    """A set of all possible price features of a FULFILMENT METHOD: default total price, discount in value or percentage etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
