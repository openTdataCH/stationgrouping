from dataclasses import dataclass, field
from typing import List

from generated.customer_purchase_package import CustomerPurchasePackage
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of CUSTOMER PURCHASE PACKAGE.
    """

    class Meta:
        name = "customerPurchasePackagesInFrame_RelStructure"

    customer_purchase_package: List[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
