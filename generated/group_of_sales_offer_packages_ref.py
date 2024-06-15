from dataclasses import dataclass

from generated.group_of_sales_offer_packages_ref_structure import (
    GroupOfSalesOfferPackagesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSalesOfferPackagesRef(GroupOfSalesOfferPackagesRefStructure):
    """
    Reference to a GROUP OF SALES OFFER PACKAGEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
