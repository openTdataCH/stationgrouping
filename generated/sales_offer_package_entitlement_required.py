from dataclasses import dataclass

from generated.sales_offer_package_entitlement_required_version_structure import (
    SalesOfferPackageEntitlementRequiredVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageEntitlementRequired(
    SalesOfferPackageEntitlementRequiredVersionStructure
):
    """
    A rerirement to a SALES OFFER PACKAGE  in order to purchase or use PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
