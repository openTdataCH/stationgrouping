from dataclasses import dataclass

from generated.security_listing_ref_structure import (
    SecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerSecurityListingRefStructure(SecurityListingRefStructure):
    """
    Type for Reference to a CUSTOMER SECURITY LISTING..
    """