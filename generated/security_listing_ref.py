from dataclasses import dataclass

from generated.security_listing_ref_structure import (
    SecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityListingRef(SecurityListingRefStructure):
    """
    Reference to a SECURITY LISTING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
