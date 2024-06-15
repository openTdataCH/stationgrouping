from dataclasses import dataclass

from generated.sales_offer_package_entitlement_given_ref_structure import (
    SalesOfferPackageEntitlementGivenRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageEntitlementGivenRef(
    SalesOfferPackageEntitlementGivenRefStructure
):
    """
    Reference to a SALES OFFER  ENTITLEMENT GIVEN PARAMETER parameter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
