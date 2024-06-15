from dataclasses import dataclass

from generated.parking_point_version_structure import (
    ParkingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPoint(ParkingPointVersionStructure):
    """A TIMING POINT where vehicles may stay unattended for a long time.

    A vehicle's return to park at a PARKING POINT marks the end of a
    BLOCK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
