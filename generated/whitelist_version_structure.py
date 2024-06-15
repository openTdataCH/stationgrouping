from dataclasses import dataclass

from generated.security_list_version_structure import (
    SecurityListVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WhitelistVersionStructure(SecurityListVersionStructure):
    """Type for WHITELIST.

    +v1.1
    """

    class Meta:
        name = "Whitelist_VersionStructure"
