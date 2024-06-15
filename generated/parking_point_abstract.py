from dataclasses import dataclass

from generated.relief_point_version_structure import (
    ReliefPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPointAbstract(ReliefPointVersionStructure):
    """A TIMING POINT where vehicles may stay unattended for a long time.

    A vehicle's return to park at a PARKING POINT marks the end of a
    BLOCK.
    """

    class Meta:
        name = "ParkingPoint_"
        namespace = "http://www.netex.org.uk/netex"
