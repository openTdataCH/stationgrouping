from dataclasses import dataclass, field
from typing import Optional

from generated.security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)
from generated.travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelDocumentSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    """
    Type for TRAVEL DOCUMENT SECURITY LISTING.
    """

    class Meta:
        name = "TravelDocumentSecurityListing_VersionedChildStructure"

    travel_document_ref: Optional[TravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
