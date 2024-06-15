from dataclasses import dataclass

from generated.stop_place_vehicle_entrance_ref_structure import (
    StopPlaceVehicleEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceVehicleEntranceRef(StopPlaceVehicleEntranceRefStructure):
    """
    Reference to a STOP PLACE VEHICLE  ENTRANCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
