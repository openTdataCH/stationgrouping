from dataclasses import dataclass

from generated.sales_offer_package_element_ref_structure import (
    SalesOfferPackageElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageElementRef(SalesOfferPackageElementRefStructure):
    """
    Reference to a SALES OFFER PACKAGE ELEMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
