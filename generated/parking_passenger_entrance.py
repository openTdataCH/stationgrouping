from dataclasses import dataclass

from generated.parking_passenger_entrance_version_structure import (
    ParkingPassengerEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPassengerEntrance(ParkingPassengerEntranceVersionStructure):
    """
    Designated Passenger ENTRANCE within a PARKING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
