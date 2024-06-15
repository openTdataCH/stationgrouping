from dataclasses import dataclass

from generated.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceRefStructure(SiteComponentRefStructure):
    """
    Type for a reference to identifier of an ENTRANCE.
    """
