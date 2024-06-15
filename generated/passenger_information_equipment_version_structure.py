from dataclasses import dataclass, field
from typing import Optional, Union

from generated.access_space_ref import AccessSpaceRef
from generated.accessibility_info_facility_list import (
    AccessibilityInfoFacilityList,
)
from generated.boarding_position_ref import BoardingPositionRef
from generated.entrance_ref import EntranceRef
from generated.logical_display_ref import LogicalDisplayRef
from generated.parking_bay_ref import ParkingBayRef
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)
from generated.parking_entrance_ref import ParkingEntranceRef
from generated.parking_passenger_entrance_ref import (
    ParkingPassengerEntranceRef,
)
from generated.passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)
from generated.passenger_information_facility_list import (
    PassengerInformationFacilityList,
)
from generated.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from generated.point_of_interest_space_ref import PointOfInterestSpaceRef
from generated.point_of_interest_vehicle_entrance_ref import (
    PointOfInterestVehicleEntranceRef,
)
from generated.quay_ref import QuayRef
from generated.site_component_ref import SiteComponentRef
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.stop_place_ref import StopPlaceRef
from generated.stop_place_space_ref import StopPlaceSpaceRef
from generated.stop_place_vehicle_entrance_ref import (
    StopPlaceVehicleEntranceRef,
)
from generated.type_of_passenger_information_equipment_ref import (
    TypeOfPassengerInformationEquipmentRef,
)
from generated.vehicle_entrance_ref import VehicleEntranceRef
from generated.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from generated.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    """
    Type for a PASSENGER INFORMATION EQUIPMENT.

    :ivar logical_display_ref:
    :ivar stop_place_ref:
    :ivar choice:
    :ivar type_of_passenger_information_equipment_ref:
    :ivar passenger_information_facility_list: List of predefined
        Passenger Info EQUIPMENT f.
    :ivar accessibility_info_facility_list:
    """

    class Meta:
        name = "PassengerInformationEquipment_VersionStructure"

    logical_display_ref: Optional[LogicalDisplayRef] = field(
        default=None,
        metadata={
            "name": "LogicalDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            VehicleStoppingPositionRef,
            VehicleStoppingPlaceRef,
            BoardingPositionRef,
            AccessSpaceRef,
            QuayRef,
            StopPlaceSpaceRef,
            ParkingBayRef,
            PointOfInterestSpaceRef,
            StopPlaceVehicleEntranceRef,
            StopPlaceEntranceRef,
            ParkingEntranceForVehiclesRef,
            ParkingPassengerEntranceRef,
            ParkingEntranceRef,
            PointOfInterestVehicleEntranceRef,
            PointOfInterestEntranceRef,
            VehicleEntranceRef,
            EntranceRef,
            SiteComponentRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleStoppingPositionRef",
                    "type": VehicleStoppingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlaceRef",
                    "type": VehicleStoppingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceSpaceRef",
                    "type": StopPlaceSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayRef",
                    "type": ParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": PointOfInterestSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "SiteComponentRef",
                    "type": SiteComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_passenger_information_equipment_ref: Optional[
        TypeOfPassengerInformationEquipmentRef
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfPassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_information_facility_list: Optional[
        PassengerInformationFacilityList
    ] = field(
        default=None,
        metadata={
            "name": "PassengerInformationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_info_facility_list: Optional[
        AccessibilityInfoFacilityList
    ] = field(
        default=None,
        metadata={
            "name": "AccessibilityInfoFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
