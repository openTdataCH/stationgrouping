from dataclasses import dataclass

from generated.retail_device_security_listing_versioned_child_structure import (
    RetailDeviceSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceSecurityListing(
    RetailDeviceSecurityListingVersionedChildStructure
):
    """
    A listing of a RETAIL DEVICE on a sSECURITY LIST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
