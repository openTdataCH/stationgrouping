from dataclasses import dataclass

from generated.relief_point_version_structure import (
    ReliefPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPointVersionStructure(ReliefPointVersionStructure):
    """
    Type for PARKING POINT.
    """

    class Meta:
        name = "ParkingPoint_VersionStructure"
