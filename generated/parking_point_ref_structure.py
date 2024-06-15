from dataclasses import dataclass

from generated.relief_point_ref_structure import ReliefPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPointRefStructure(ReliefPointRefStructure):
    """
    Type for a reference to a PARKING POINT.
    """
