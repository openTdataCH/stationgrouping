from dataclasses import dataclass

from generated.parking_capacity_ref_structure import (
    ParkingCapacityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingCapacityRef(ParkingCapacityRefStructure):
    """
    Reference to a PARKING CAPACITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
