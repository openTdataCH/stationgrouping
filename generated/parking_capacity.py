from dataclasses import dataclass

from generated.parking_capacity_versioned_child_structure import (
    ParkingCapacityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingCapacity(ParkingCapacityVersionedChildStructure):
    """
    Capacity of a PARKING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
