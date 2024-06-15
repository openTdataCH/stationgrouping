from dataclasses import dataclass

from generated.validable_element_price_versioned_child_structure import (
    ValidableElementPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementPrice(ValidableElementPriceVersionedChildStructure):
    """A set of all possible price features of a VALIDABLE ELEMENT ELEMENT: default total price, discount in value or percentage etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
