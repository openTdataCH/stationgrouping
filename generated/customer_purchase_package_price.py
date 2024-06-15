from dataclasses import dataclass

from generated.customer_purchase_package_price_versioned_child_structure import (
    CustomerPurchasePackagePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagePrice(
    CustomerPurchasePackagePriceVersionedChildStructure
):
    """A set of all possible price features of a CUSTOMER PURCHASE PACKAGE ELEMENT: default total price, discount in value or percentage etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
