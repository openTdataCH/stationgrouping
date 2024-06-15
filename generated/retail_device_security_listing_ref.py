from dataclasses import dataclass

from generated.retail_device_security_listing_ref_structure import (
    RetailDeviceSecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceSecurityListingRef(RetailDeviceSecurityListingRefStructure):
    """
    Reference to a RETAIL DEVICE SECURITY LISTING..
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
