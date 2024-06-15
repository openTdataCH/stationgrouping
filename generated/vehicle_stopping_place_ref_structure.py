from dataclasses import dataclass

from generated.stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlaceRefStructure(StopPlaceSpaceRefStructure):
    """
    Type for reference to a VEHICLE STOPPING PLACE.
    """
