from dataclasses import dataclass

from generated.customer_account_security_listing_ref_structure import (
    CustomerAccountSecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountSecurityListingRef(
    CustomerAccountSecurityListingRefStructure
):
    """
    Reference to a CUSTOMER ACCOUNT SECURITY LISTING..
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
