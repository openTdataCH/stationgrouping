from dataclasses import dataclass, field
from typing import Optional

from generated.customer_account_ref import CustomerAccountRef
from generated.security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    """
    Type for CUSTOMER ACCOUNT SECURITY LISTING.
    """

    class Meta:
        name = "CustomerAccountSecurityListing_VersionedChildStructure"

    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
