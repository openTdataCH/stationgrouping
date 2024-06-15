from dataclasses import dataclass

from generated.entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityListing2(VersionedChildStructure):
    """
    DUMMY type for SECIRITY LISTING.
    """

    class Meta:
        name = "SecurityListing_"
        namespace = "http://www.netex.org.uk/netex"
