from dataclasses import dataclass

from generated.parking_point_version_structure import (
    ParkingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePointVersionStructure(ParkingPointVersionStructure):
    """
    Type for GARAGE POINT.
    """

    class Meta:
        name = "GaragePoint_VersionStructure"
