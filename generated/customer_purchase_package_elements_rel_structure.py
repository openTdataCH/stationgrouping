from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.customer_purchase_package_element import (
    CustomerPurchasePackageElement,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElementsRelStructure(
    ContainmentAggregationStructure
):
    """
    Type for a list of CUSTOMER PURCHASE PACKAGE ELEMENTs.
    """

    class Meta:
        name = "customerPurchasePackageElements_RelStructure"

    customer_purchase_package_element: List[CustomerPurchasePackageElement] = (
        field(
            default_factory=list,
            metadata={
                "name": "CustomerPurchasePackageElement",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
