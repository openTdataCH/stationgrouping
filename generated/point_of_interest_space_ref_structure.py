from dataclasses import dataclass

from generated.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestSpaceRefStructure(SiteComponentRefStructure):
    """
    Type for reference to a POINT OF INTEREST SPACE.
    """
