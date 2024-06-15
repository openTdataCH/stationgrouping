from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.parking_capacity import ParkingCapacity
from generated.parking_capacity_ref import ParkingCapacityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingCapacitiesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING CAPACITies.
    """

    class Meta:
        name = "parkingCapacities_RelStructure"

    parking_capacity_ref_or_parking_capacity: List[
        Union[ParkingCapacityRef, ParkingCapacity]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingCapacityRef",
                    "type": ParkingCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingCapacity",
                    "type": ParkingCapacity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
