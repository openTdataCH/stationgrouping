from dataclasses import dataclass

from generated.parking_point_ref_structure import ParkingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPointRef(ParkingPointRefStructure):
    """
    Reference to a PARKING POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
