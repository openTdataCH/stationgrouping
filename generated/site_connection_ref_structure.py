from dataclasses import dataclass

from generated.connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteConnectionRefStructure(ConnectionRefStructure):
    """
    Type for a reference to a SITE CONNECTION link.
    """
