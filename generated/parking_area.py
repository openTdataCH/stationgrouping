from dataclasses import dataclass

from generated.parking_area_version_structure import (
    ParkingAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingArea(ParkingAreaVersionStructure):
    """
    Area within a PARKING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"