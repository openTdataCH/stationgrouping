from dataclasses import dataclass, field
from typing import Optional, Union

from generated.blacklist_ref import BlacklistRef
from generated.entity_in_version_structure import VersionedChildStructure
from generated.multilingual_string import MultilingualString
from generated.whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityListingVersionedChildStructure(VersionedChildStructure):
    """
    Type for SECURITY LISTING.

    :ivar name: Name of SECURITY LISTING.
    :ivar whitelist_ref_or_blacklist_ref:
    :ivar order: order within list
    """

    class Meta:
        name = "SecurityListing_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    whitelist_ref_or_blacklist_ref: Optional[
        Union[WhitelistRef, BlacklistRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
