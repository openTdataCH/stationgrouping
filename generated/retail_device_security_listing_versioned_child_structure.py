from dataclasses import dataclass, field
from typing import Optional

from generated.retail_device_ref import RetailDeviceRef
from generated.security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    """
    Type for  RETAIL DEVICE SECURITY LISTING.
    """

    class Meta:
        name = "RetailDeviceSecurityListing_VersionedChildStructure"

    retail_device_ref: Optional[RetailDeviceRef] = field(
        default=None,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
