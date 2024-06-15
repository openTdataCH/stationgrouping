from dataclasses import dataclass

from generated.customer_security_listing_versioned_child_structure import (
    CustomerSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerSecurityListing(CustomerSecurityListingVersionedChildStructure):
    """
    A listing of a CUSTOMER on a SECURITY LIST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
