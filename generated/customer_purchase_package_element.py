from dataclasses import dataclass

from generated.customer_purchase_package_element_version_structure import (
    CustomerPurchasePackageElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElement(
    CustomerPurchasePackageElementVersionStructure
):
    """
    The assignment of a  SALES OFFER PACKAGE ELEMENT, for use in a CUSTOMER SALES
    PACKAGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
