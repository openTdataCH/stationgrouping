from dataclasses import dataclass

from generated.customer_purchase_package_ref_structure import (
    CustomerPurchasePackageRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageRef(CustomerPurchasePackageRefStructure):
    """
    Reference to a CUSTOMER PURCHASE PACKAGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
