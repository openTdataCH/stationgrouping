from dataclasses import dataclass

from generated.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayRefStructure(SiteComponentRefStructure):
    """
    Type for a reference to a PARKING BAY.
    """
