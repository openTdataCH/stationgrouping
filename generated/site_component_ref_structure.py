from dataclasses import dataclass

from generated.site_element_ref_structure import SiteElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteComponentRefStructure(SiteElementRefStructure):
    """
    Type for reference to a SITE COMPONENT.
    """
