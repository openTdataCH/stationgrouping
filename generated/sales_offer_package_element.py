from dataclasses import dataclass

from generated.sales_offer_package_element_version_structure import (
    SalesOfferPackageElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageElement(SalesOfferPackageElementVersionStructure):
    """
    The assignment of a FARE PRODUCT to a TYPE OF TRAVEL DOCUMENT in order to
    define a SALES OFFER PACKAGE, realised as a fixed assignment (printing,
    magnetic storage etc.) or by the possibility for the FARE PRODUCT to be
    reloaded on the TYPE OF TRAVEL DOCUMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
