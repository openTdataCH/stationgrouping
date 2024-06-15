from dataclasses import dataclass

from generated.travel_document_security_listing_versioned_child_structure import (
    TravelDocumentSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelDocumentSecurityListing(
    TravelDocumentSecurityListingVersionedChildStructure
):
    """
    A listing of a TRAVEL DOCUMENT on a SECURITY LIST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
