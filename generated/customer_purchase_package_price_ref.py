from dataclasses import dataclass

from generated.customer_purchase_package_price_ref_structure import (
    CustomerPurchasePackagePriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagePriceRef(
    CustomerPurchasePackagePriceRefStructure
):
    """
    Reference to a CUSTOMER PURCHASE PACKAGE PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
