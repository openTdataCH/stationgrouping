from dataclasses import dataclass, field
from typing import List, Union

from generated.cell_ref import CellRef
from generated.customer_purchase_package_price_ref import (
    CustomerPurchasePackagePriceRef,
)
from generated.customer_purchase_package_price_versioned_child_structure import (
    CustomerPurchasePackagePriceVersionedChildStructure,
)
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagePricesRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of CUSTOMER PURCHASE PACKAGE PRICEs.
    """

    class Meta:
        name = "customerPurchasePackagePrices_RelStructure"

    customer_purchase_package_price_ref_or_customer_purchase_package_price_or_cell_ref: List[
        Union[
            CustomerPurchasePackagePriceRef,
            CustomerPurchasePackagePriceVersionedChildStructure,
            CellRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePriceVersionedChildStructure,
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