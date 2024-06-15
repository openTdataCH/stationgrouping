from dataclasses import dataclass, field
from typing import Optional

from generated.blacklist_refs_rel_structure import BlacklistRefsRelStructure
from generated.organisation_refs_rel_structure import (
    OrganisationRefsRelStructure,
)
from generated.organisation_version_structure import (
    OrganisationVersionStructure,
)
from generated.postal_address import PostalAddress
from generated.retail_devices_rel_structure import RetailDevicesRelStructure
from generated.whitelist_refs_rel_structure import WhitelistRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailConsortiumVersionStructure(OrganisationVersionStructure):
    """
    Type for RETAIL CONSORTIUM.

    :ivar postal_address:
    :ivar members: RETAIL DEVICEs used by to RETAIL CONSORTIUM.
    :ivar blacklist_refs: BLACKLISTs used by RETAIL CONSORTIUM.
    :ivar whitelist_refs: WHITELISTs used by RETAIL CONSORTIUM.
    :ivar retail_devices: RETAIL DEVICEs used by RETAIL CONSORTIUM.
    """

    class Meta:
        name = "RetailConsortium_VersionStructure"

    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blacklist_refs: Optional[BlacklistRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "blacklistRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    whitelist_refs: Optional[WhitelistRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "whitelistRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_devices: Optional[RetailDevicesRelStructure] = field(
        default=None,
        metadata={
            "name": "retailDevices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
