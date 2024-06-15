from dataclasses import dataclass

from generated.parking_ref_structure import ParkingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingRef(ParkingRefStructure):
    """
    Reference to a PARKING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
