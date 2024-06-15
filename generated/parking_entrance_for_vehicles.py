from dataclasses import dataclass

from generated.parking_entrance_for_vehicles_version_structure import (
    ParkingEntranceForVehiclesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingEntranceForVehicles(ParkingEntranceForVehiclesVersionStructure):
    """
    Designated Place within a PARKING for a VEHICLE to enter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
