from dataclasses import dataclass

from generated.parking_entrance_for_vehicles_ref_structure import (
    ParkingEntranceForVehiclesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingEntranceForVehiclesRef(ParkingEntranceForVehiclesRefStructure):
    """
    Reference to a PARKING VEHICLE ENTRANCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
