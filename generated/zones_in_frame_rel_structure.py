from dataclasses import dataclass, field
from typing import List, Union

from generated.access_space import AccessSpace
from generated.access_zone import AccessZone
from generated.addressable_place import AddressablePlace
from generated.administrative_zones_rel_structure import (
    AdministrativeZone,
    TransportAdministrativeZone,
)
from generated.boarding_position import BoardingPosition
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.country import Country
from generated.entrance import Entrance
from generated.equipment_place import EquipmentPlace
from generated.fare_zone import FareZone
from generated.flexible_area import FlexibleArea
from generated.flexible_quay import FlexibleQuay
from generated.flexible_stop_place import FlexibleStopPlace
from generated.garage import Garage
from generated.general_zone import GeneralZone
from generated.hail_and_ride_area import HailAndRideArea
from generated.parking import Parking
from generated.parking_area import ParkingArea
from generated.parking_bay import ParkingBay
from generated.parking_component import ParkingComponent
from generated.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from generated.parking_passenger_entrance import ParkingPassengerEntrance
from generated.point_of_interest import PointOfInterest
from generated.point_of_interest_entrance import PointOfInterestEntrance
from generated.point_of_interest_space import PointOfInterestSpace
from generated.point_of_interest_vehicle_entrance import (
    PointOfInterestVehicleEntrance,
)
from generated.postal_address import PostalAddress
from generated.quay import Quay
from generated.road_address import RoadAddress
from generated.routing_constraint_zone import RoutingConstraintZone
from generated.service_site import ServiceSite
from generated.stop_area import StopArea
from generated.stop_place import StopPlace
from generated.stop_place_entrance import StopPlaceEntrance
from generated.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from generated.tariff_zone import TariffZone
from generated.topographic_place import TopographicPlace
from generated.vehicle_stopping_place import VehicleStoppingPlace
from generated.vehicle_stopping_position import VehicleStoppingPosition
from generated.zone import Zone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZonesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ZONEs.
    """

    class Meta:
        name = "zonesInFrame_RelStructure"

    choice: List[
        Union[
            RoutingConstraintZone,
            StopArea,
            AccessZone,
            HailAndRideArea,
            FlexibleArea,
            FlexibleQuay,
            FlexibleStopPlace,
            VehicleStoppingPlace,
            BoardingPosition,
            AccessSpace,
            Quay,
            PointOfInterestSpace,
            ParkingBay,
            ParkingArea,
            ParkingComponent,
            VehicleStoppingPosition,
            PointOfInterestVehicleEntrance,
            PointOfInterestEntrance,
            ParkingPassengerEntrance,
            ParkingEntranceForVehicles,
            StopPlaceVehicleEntrance,
            StopPlaceEntrance,
            Entrance,
            PointOfInterest,
            Parking,
            StopPlace,
            ServiceSite,
            Garage,
            TopographicPlace,
            EquipmentPlace,
            Country,
            AddressablePlace,
            PostalAddress,
            RoadAddress,
            TransportAdministrativeZone,
            AdministrativeZone,
            FareZone,
            TariffZone,
            GeneralZone,
            Zone,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RoutingConstraintZone",
                    "type": RoutingConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopArea",
                    "type": StopArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZone",
                    "type": AccessZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HailAndRideArea",
                    "type": HailAndRideArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleArea",
                    "type": FlexibleArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuay",
                    "type": FlexibleQuay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlace",
                    "type": FlexibleStopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlace",
                    "type": VehicleStoppingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpace",
                    "type": AccessSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpace",
                    "type": PointOfInterestSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBay",
                    "type": ParkingBay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingComponent",
                    "type": ParkingComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPosition",
                    "type": VehicleStoppingPosition,
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
                {
                    "name": "PointOfInterest",
                    "type": PointOfInterest,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Parking",
                    "type": Parking,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSite",
                    "type": ServiceSite,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Garage",
                    "type": Garage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlace",
                    "type": TopographicPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlace",
                    "type": EquipmentPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Country",
                    "type": Country,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressablePlace",
                    "type": AddressablePlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZone",
                    "type": TransportAdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": AdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZone",
                    "type": FareZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZone",
                    "type": TariffZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralZone",
                    "type": GeneralZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Zone",
                    "type": Zone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
