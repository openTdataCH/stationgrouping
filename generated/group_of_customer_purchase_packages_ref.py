from dataclasses import dataclass

from generated.group_of_customer_purchase_packages_ref_structure import (
    GroupOfCustomerPurchasePackagesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfCustomerPurchasePackagesRef(
    GroupOfCustomerPurchasePackagesRefStructure
):
    """
    Reference to a GROUP OF CUSTOMER PURCHASE PACKAGEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
