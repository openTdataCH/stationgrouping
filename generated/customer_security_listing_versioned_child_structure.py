from dataclasses import dataclass, field
from typing import Optional

from generated.customer_ref import CustomerRef
from generated.security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    """
    Type for CUSTOMER SECURITY LISTING.
    """

    class Meta:
        name = "CustomerSecurityListing_VersionedChildStructure"

    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
