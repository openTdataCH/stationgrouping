from dataclasses import dataclass

from generated.site_element_ref_structure import SiteElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteRefStructure(SiteElementRefStructure):
    """
    Type for identifier of a SITE.
    """
