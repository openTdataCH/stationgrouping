from dataclasses import dataclass

from generated.security_listing_ref_structure import (
    SecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelDocumentSecurityListingRefStructure(SecurityListingRefStructure):
    """
    Type for Reference to a TRAVEL DOCUMENT SECURITY LISTING..
    """
