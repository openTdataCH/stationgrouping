from dataclasses import dataclass

from generated.customer_account_security_listing_versioned_child_structure import (
    CustomerAccountSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountSecurityListing(
    CustomerAccountSecurityListingVersionedChildStructure
):
    """
    A listing of a CUSTOMER ACCOUNT on a SECURITY LIST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
