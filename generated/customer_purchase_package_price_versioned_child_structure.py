from dataclasses import dataclass, field
from typing import Optional, Union

from generated.customer_purchase_package_element_ref import (
    CustomerPurchasePackageElementRef,
)
from generated.customer_purchase_package_ref import CustomerPurchasePackageRef
from generated.fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagePriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    """
    Type for a CUSTOMER PURCHASE PACKAGE PRICEs.
    """

    class Meta:
        name = "CustomerPurchasePackagePrice_VersionedChildStructure"

    customer_purchase_package_ref_or_customer_purchase_package_element_ref: Optional[
        Union[CustomerPurchasePackageRef, CustomerPurchasePackageElementRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElementRef",
                    "type": CustomerPurchasePackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
