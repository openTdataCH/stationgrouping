from dataclasses import dataclass

from generated.parking_entrance_ref_structure import (
    ParkingEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPassengerEntranceRefStructure(ParkingEntranceRefStructure):
    """
    Type for reference to a PARKING ENTRANCE.
    """