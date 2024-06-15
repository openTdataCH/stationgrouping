from dataclasses import dataclass

from generated.parking_passenger_entrance_ref_structure import (
    ParkingPassengerEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPassengerEntranceRef(ParkingPassengerEntranceRefStructure):
    """
    Reference to a PARKING VEHICLE ENTRANCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
