from dataclasses import dataclass

from generated.security_list_ref_structure import SecurityListRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlacklistRefStructure(SecurityListRefStructure):
    """
    Type for Reference to a BLACKLIST.
    """
