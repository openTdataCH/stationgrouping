from dataclasses import dataclass, field
from typing import List, Union

from generated.access_space_ref import AccessSpaceRef
from generated.address_ref import AddressRef
from generated.addressable_place_ref import AddressablePlaceRef
from generated.boarding_position_ref import BoardingPositionRef
from generated.entrance_ref import EntranceRef
from generated.equipment_place_ref import EquipmentPlaceRef
from generated.equipment_position_ref import EquipmentPositionRef
from generated.flexible_area_ref import FlexibleAreaRef
from generated.flexible_quay_ref import FlexibleQuayRef
from generated.flexible_stop_place_ref import FlexibleStopPlaceRef
from generated.garage_ref import GarageRef
from generated.hail_and_ride_area_ref import HailAndRideAreaRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.parking_bay_ref import ParkingBayRef
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)
from generated.parking_entrance_ref import ParkingEntranceRef
from generated.parking_passenger_entrance_ref import (
    ParkingPassengerEntranceRef,
)
from generated.parking_ref import ParkingRef
from generated.path_junction_ref import PathJunctionRef
from generated.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from generated.point_of_interest_ref import PointOfInterestRef
from generated.point_of_interest_space_ref import PointOfInterestSpaceRef
from generated.point_of_interest_vehicle_entrance_ref import (
    PointOfInterestVehicleEntranceRef,
)
from generated.postal_address_ref import PostalAddressRef
from generated.quay_ref import QuayRef
from generated.road_address_ref import RoadAddressRef
from generated.service_site_ref import ServiceSiteRef
from generated.site_component_ref import SiteComponentRef
from generated.site_element_ref import SiteElementRef
from generated.site_ref import SiteRef
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.stop_place_ref import StopPlaceRef
from generated.stop_place_space_ref import StopPlaceSpaceRef
from generated.stop_place_vehicle_entrance_ref import (
    StopPlaceVehicleEntranceRef,
)
from generated.topographic_place_ref import TopographicPlaceRef
from generated.vehicle_entrance_ref import VehicleEntranceRef
from generated.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from generated.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DummyPlaceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a PLACE.
    """

    class Meta:
        name = "dummyPlaceRefs_RelStructure"

    choice: List[
        Union[
            HailAndRideAreaRef,
            FlexibleAreaRef,
            FlexibleQuayRef,
            FlexibleStopPlaceRef,
            PathJunctionRef,
            TopographicPlaceRef,
            EquipmentPlaceRef,
            EquipmentPositionRef,
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
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
            SiteElementRef,
            GarageRef,
            AddressablePlaceRef,
            PostalAddressRef,
            RoadAddressRef,
            AddressRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuayRef",
                    "type": FlexibleQuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlaceRef",
                    "type": FlexibleStopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunctionRef",
                    "type": PathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlaceRef",
                    "type": EquipmentPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPositionRef",
                    "type": EquipmentPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteElementRef",
                    "type": SiteElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GarageRef",
                    "type": GarageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressablePlaceRef",
                    "type": AddressablePlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PostalAddressRef",
                    "type": PostalAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddressRef",
                    "type": RoadAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressRef",
                    "type": AddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
