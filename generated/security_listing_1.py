from dataclasses import dataclass

from generated.security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityListing1(SecurityListingVersionedChildStructure):
    """
    The presence of an identified Entity on a SECURITY LIST.
    """

    class Meta:
        name = "SecurityListing"
        namespace = "http://www.netex.org.uk/netex"
