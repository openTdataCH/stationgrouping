from dataclasses import dataclass

from generated.parking_entrance_ref_structure import (
    ParkingEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingEntranceRef(ParkingEntranceRefStructure):
    """
    Reference to a PARKING VEHICLE ENTRANCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
