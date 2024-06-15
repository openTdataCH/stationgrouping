from dataclasses import dataclass, field
from typing import List, Union

from generated.entrance_ref import EntranceRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)
from generated.parking_entrance_ref import ParkingEntranceRef
from generated.parking_passenger_entrance_ref import (
    ParkingPassengerEntranceRef,
)
from generated.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from generated.point_of_interest_vehicle_entrance_ref import (
    PointOfInterestVehicleEntranceRef,
)
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.stop_place_vehicle_entrance_ref import (
    StopPlaceVehicleEntranceRef,
)
from generated.vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more ENTRANCEs.
    """

    class Meta:
        name = "entranceRefs_RelStructure"

    choice: List[
        Union[
            StopPlaceVehicleEntranceRef,
            StopPlaceEntranceRef,
            ParkingEntranceForVehiclesRef,
            ParkingPassengerEntranceRef,
            ParkingEntranceRef,
            PointOfInterestVehicleEntranceRef,
            PointOfInterestEntranceRef,
            VehicleEntranceRef,
            EntranceRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceVehicleEntranceRef",
                    "type": StopPlaceVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntranceRef",
                    "type": StopPlaceEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehiclesRef",
                    "type": ParkingEntranceForVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntranceRef",
                    "type": ParkingPassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceRef",
                    "type": ParkingEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestVehicleEntranceRef",
                    "type": PointOfInterestVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntranceRef",
                    "type": PointOfInterestEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEntranceRef",
                    "type": VehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceRef",
                    "type": EntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
