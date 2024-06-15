from dataclasses import dataclass

from generated.site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceRefStructure(SiteRefStructure):
    """
    Type for a reference to a STOP PLACE.
    """
