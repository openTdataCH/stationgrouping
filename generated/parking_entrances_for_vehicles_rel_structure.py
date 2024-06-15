from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingEntrancesForVehiclesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING ENTRANCE.
    """

    class Meta:
        name = "parkingEntrancesForVehicles_RelStructure"

    parking_entrance_for_vehicles_ref_or_parking_entrance_for_vehicles: List[
        Union[ParkingEntranceForVehiclesRef, ParkingEntranceForVehicles]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingEntranceForVehiclesRef",
                    "type": ParkingEntranceForVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehicles",
                    "type": ParkingEntranceForVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
