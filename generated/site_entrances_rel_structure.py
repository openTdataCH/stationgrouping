from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.entrance import Entrance
from generated.entrance_ref import EntranceRef
from generated.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)
from generated.parking_entrance_ref import ParkingEntranceRef
from generated.parking_passenger_entrance import ParkingPassengerEntrance
from generated.parking_passenger_entrance_ref import (
    ParkingPassengerEntranceRef,
)
from generated.point_of_interest_entrance import PointOfInterestEntrance
from generated.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from generated.point_of_interest_vehicle_entrance import (
    PointOfInterestVehicleEntrance,
)
from generated.point_of_interest_vehicle_entrance_ref import (
    PointOfInterestVehicleEntranceRef,
)
from generated.stop_place_entrance import StopPlaceEntrance
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from generated.stop_place_vehicle_entrance_ref import (
    StopPlaceVehicleEntranceRef,
)
from generated.vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteEntrancesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ENTRANCEs.
    """

    class Meta:
        name = "siteEntrances_RelStructure"

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
            PointOfInterestVehicleEntrance,
            PointOfInterestEntrance,
            ParkingPassengerEntrance,
            ParkingEntranceForVehicles,
            StopPlaceVehicleEntrance,
            StopPlaceEntrance,
            Entrance,
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
                {
                    "name": "PointOfInterestVehicleEntrance",
                    "type": PointOfInterestVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntrance",
                    "type": PointOfInterestEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntrance",
                    "type": ParkingPassengerEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehicles",
                    "type": ParkingEntranceForVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntrance",
                    "type": StopPlaceVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntrance",
                    "type": StopPlaceEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Entrance",
                    "type": Entrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
