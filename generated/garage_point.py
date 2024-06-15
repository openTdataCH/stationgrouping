from dataclasses import dataclass

from generated.parking_point_version_structure import (
    ParkingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePoint(ParkingPointVersionStructure):
    """
    A subtype of PARKING POINT located in a GARAGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
