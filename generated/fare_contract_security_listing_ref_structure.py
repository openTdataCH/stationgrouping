from dataclasses import dataclass

from generated.security_listing_ref_structure import (
    SecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractSecurityListingRefStructure(SecurityListingRefStructure):
    """
    Type for Reference to a FARE CONTRACT SECURITY LISTING..
    """
