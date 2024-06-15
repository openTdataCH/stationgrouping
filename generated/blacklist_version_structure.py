from dataclasses import dataclass

from generated.security_list_version_structure import (
    SecurityListVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlacklistVersionStructure(SecurityListVersionStructure):
    """
    Type for BLACKLIST.
    """

    class Meta:
        name = "Blacklist_VersionStructure"
