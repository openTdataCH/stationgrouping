from dataclasses import dataclass, field
from typing import Optional

from generated.navigation_paths_rel_structure import (
    NavigationPathsRelStructure,
)
from generated.site_connection_end_structure import SiteConnectionEndStructure
from generated.transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteConnectionVersionStructure(TransferVersionStructure):
    """
    Type for a SITE CONNECTION.

    :ivar from_value: Origin end of SITE CONNECTION.
    :ivar to: Destination end of SITE CONNECTION.
    :ivar navigation_paths: NAVIGATION PATHs between SITEs.
    """

    class Meta:
        name = "SiteConnection_VersionStructure"

    from_value: Optional[SiteConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to: Optional[SiteConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
