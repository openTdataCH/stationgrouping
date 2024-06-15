from dataclasses import dataclass

from generated.parking_point_ref_structure import ParkingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePointRefStructure(ParkingPointRefStructure):
    """
    Type for a reference to a GARAGE POINT.
    """
