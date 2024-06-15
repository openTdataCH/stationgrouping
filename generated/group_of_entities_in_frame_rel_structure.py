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
from generated.crew_base import CrewBase
from generated.entrance import Entrance
from generated.equipment_place import EquipmentPlace
from generated.fare_zone import FareZone
from generated.flexible_area import FlexibleArea
from generated.flexible_quay import FlexibleQuay
from generated.flexible_stop_place import FlexibleStopPlace
from generated.garage import Garage
from generated.general_group_of_entities import GeneralGroupOfEntities
from generated.general_zone import GeneralZone
from generated.group_of_distance_matrix_elements import (
    GroupOfDistanceMatrixElements,
)
from generated.group_of_distribution_channels import (
    GroupOfDistributionChannels,
)
from generated.group_of_lines import GroupOfLines
from generated.group_of_link_sequences import GroupOfLinkSequences
from generated.group_of_links import GroupOfLinks
from generated.group_of_operators import GroupOfOperators
from generated.group_of_places import GroupOfPlaces
from generated.group_of_points import GroupOfPoints
from generated.group_of_services import GroupOfServices
from generated.group_of_timing_links import GroupOfTimingLinks
from generated.hail_and_ride_area import HailAndRideArea
from generated.headway_journey_group import HeadwayJourneyGroup
from generated.layer import Layer
from generated.network import Network
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
from generated.priceable_object_version_structure import (
    FareTable,
    FareTableInContext,
    PriceGroup,
)
from generated.quay import Quay
from generated.rhythmical_journey_group import RhythmicalJourneyGroup
from generated.road_address import RoadAddress
from generated.routing_constraint_zone import RoutingConstraintZone
from generated.service_site import ServiceSite
from generated.standard_fare_table import StandardFareTable
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
class GroupOfEntitiesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GROUP OF ENTITIes.
    """

    class Meta:
        name = "groupOfEntitiesInFrame_RelStructure"

    choice: List[
        Union[
            GroupOfDistributionChannels,
            GroupOfDistanceMatrixElements,
            PriceGroup,
            StandardFareTable,
            FareTableInContext,
            FareTable,
            GroupOfServices,
            RhythmicalJourneyGroup,
            HeadwayJourneyGroup,
            Network,
            GroupOfLines,
            CrewBase,
            GroupOfTimingLinks,
            GroupOfOperators,
            GroupOfPlaces,
            GroupOfLinkSequences,
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
            GroupOfLinks,
            GroupOfPoints,
            Layer,
            GeneralGroupOfEntities,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfDistributionChannels",
                    "type": GroupOfDistributionChannels,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElements",
                    "type": GroupOfDistanceMatrixElements,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroup",
                    "type": PriceGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServices",
                    "type": GroupOfServices,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroup",
                    "type": RhythmicalJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroup",
                    "type": HeadwayJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Network",
                    "type": Network,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLines",
                    "type": GroupOfLines,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrewBase",
                    "type": CrewBase,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimingLinks",
                    "type": GroupOfTimingLinks,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperators",
                    "type": GroupOfOperators,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPlaces",
                    "type": GroupOfPlaces,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinkSequences",
                    "type": GroupOfLinkSequences,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GroupOfLinks",
                    "type": GroupOfLinks,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPoints",
                    "type": GroupOfPoints,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Layer",
                    "type": Layer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralGroupOfEntities",
                    "type": GeneralGroupOfEntities,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
