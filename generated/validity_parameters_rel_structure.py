from dataclasses import dataclass, field
from typing import List, Union

from generated.access_space_ref import AccessSpaceRef
from generated.address_ref import AddressRef
from generated.all_authorities_ref import AllAuthoritiesRef
from generated.all_operators_ref import AllOperatorsRef
from generated.authority_ref import AuthorityRef
from generated.boarding_position_ref import BoardingPositionRef
from generated.charging_moment_ref import ChargingMomentRef
from generated.class_of_use_ref import ClassOfUseRef
from generated.compound_train_ref import CompoundTrainRef
from generated.discounting_rule_ref import DiscountingRuleRef
from generated.distribution_channel_ref import DistributionChannelRef
from generated.entrance_ref import EntranceRef
from generated.facility_set_ref import FacilitySetRef
from generated.fare_class import FareClass
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.fare_section_ref import FareSectionRef
from generated.fare_zone_ref import FareZoneRef
from generated.flexible_line_ref import FlexibleLineRef
from generated.fulfilment_method_ref import FulfilmentMethodRef
from generated.group_of_distribution_channels_ref import (
    GroupOfDistributionChannelsRef,
)
from generated.group_of_lines_ref import GroupOfLinesRef
from generated.group_of_operators_ref import GroupOfOperatorsRef
from generated.group_of_services_ref import GroupOfServicesRef
from generated.limiting_rule_ref import LimitingRuleRef
from generated.line_ref import LineRef
from generated.network_ref import NetworkRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.operator_ref import OperatorRef
from generated.parking_bay_ref import ParkingBayRef
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)
from generated.parking_entrance_ref import ParkingEntranceRef
from generated.parking_passenger_entrance_ref import (
    ParkingPassengerEntranceRef,
)
from generated.parking_ref import ParkingRef
from generated.passenger_seat_ref import PassengerSeatRef
from generated.place_use_enumeration import PlaceUseEnumeration
from generated.point_of_interest_classification_ref import (
    PointOfInterestClassificationRef,
)
from generated.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from generated.point_of_interest_ref import PointOfInterestRef
from generated.point_of_interest_space_ref import PointOfInterestSpaceRef
from generated.point_of_interest_vehicle_entrance_ref import (
    PointOfInterestVehicleEntranceRef,
)
from generated.postal_address_ref import PostalAddressRef
from generated.pricing_rule_ref import PricingRuleRef
from generated.quay_ref import QuayRef
from generated.relative_direction_enumeration import (
    RelativeDirectionEnumeration,
)
from generated.road_address_ref import RoadAddressRef
from generated.routing_type_enumeration import RoutingTypeEnumeration
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.series_constraint_ref import SeriesConstraintRef
from generated.service_facility_set_ref import ServiceFacilitySetRef
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_journey_ref import ServiceJourneyRef
from generated.service_site_ref import ServiceSiteRef
from generated.site_component_ref import SiteComponentRef
from generated.site_element_ref import SiteElementRef
from generated.site_facility_set_ref import SiteFacilitySetRef
from generated.site_ref import SiteRef
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.stop_place_ref import StopPlaceRef
from generated.stop_place_space_ref import StopPlaceSpaceRef
from generated.stop_place_vehicle_entrance_ref import (
    StopPlaceVehicleEntranceRef,
)
from generated.tariff_zone_ref import TariffZoneRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.topographic_place_ref import TopographicPlaceRef
from generated.train_component_label_assignment_ref import (
    TrainComponentLabelAssignmentRef,
)
from generated.train_element_ref import TrainElementRef
from generated.train_number_ref import TrainNumberRef
from generated.train_ref import TrainRef
from generated.transport_submode import TransportSubmode
from generated.type_of_concession_ref import TypeOfConcessionRef
from generated.type_of_fare_product_ref import TypeOfFareProductRef
from generated.type_of_fare_structure_element_ref import (
    TypeOfFareStructureElementRef,
)
from generated.type_of_fare_structure_factor_ref import (
    TypeOfFareStructureFactorRef,
)
from generated.type_of_line_ref import TypeOfLineRef
from generated.type_of_machine_readability_ref import (
    TypeOfMachineReadabilityRef,
)
from generated.type_of_payment_method_ref import TypeOfPaymentMethodRef
from generated.type_of_pricing_rule_ref import TypeOfPricingRuleRef
from generated.type_of_product_category_ref import TypeOfProductCategoryRef
from generated.type_of_sales_offer_package_ref import (
    TypeOfSalesOfferPackageRef,
)
from generated.type_of_service_ref import TypeOfServiceRef
from generated.type_of_tariff_ref import TypeOfTariffRef
from generated.type_of_travel_document_ref import TypeOfTravelDocumentRef
from generated.type_of_usage_parameter_ref import TypeOfUsageParameterRef
from generated.vehicle_entrance_ref import VehicleEntranceRef
from generated.vehicle_mode_enumeration import VehicleModeEnumeration
from generated.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from generated.vehicle_stopping_position_ref import VehicleStoppingPositionRef
from generated.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityParametersRelStructure(OneToManyRelationshipStructure):
    """
    One to many Relationship for scoping validity parameters.

    :ivar vehicle_modes: Vehicle Modes to which ACCESS RIGHTs apply.
    :ivar transport_submode:
    :ivar group_of_operators_ref:
    :ivar all_operators_ref_or_operator_ref:
    :ivar all_authorities_ref_or_authority_ref:
    :ivar network_ref_or_group_of_lines_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar type_of_line_ref:
    :ivar tariff_zone_ref:
    :ivar fare_zone_ref:
    :ivar fare_section_ref:
    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar place_use: Use of PLACE.
    :ivar topographic_place_ref:
    :ivar postal_address_ref_or_road_address_ref_or_address_ref:
    :ivar choice:
    :ivar point_of_interest_classification_ref:
    :ivar routing_type: Whether this is a direct i.e. no changes
        required point to point or indirect.
    :ivar directions: Whether use SERIES, or FARE SECTION in forwards,
        backwards or both directions.
    :ivar series_constraint_ref:
    :ivar service_journey_pattern_ref:
    :ivar class_of_use_ref:
    :ivar fare_class:
    :ivar
        service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref:
    :ivar type_of_product_category_ref:
    :ivar template_service_journey_ref_or_service_journey_ref:
    :ivar train_number_ref:
    :ivar group_of_services_ref:
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    :ivar type_of_service_ref:
    :ivar train_element_ref:
    :ivar train_component_label_assignment_ref:
    :ivar passenger_seat_ref:
    :ivar type_of_fare_structure_factor_ref:
    :ivar type_of_fare_structure_element_ref:
    :ivar type_of_tariff_ref:
    :ivar limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref:
    :ivar type_of_pricing_rule_ref:
    :ivar charging_moment_ref:
    :ivar type_of_fare_product_ref:
    :ivar type_of_usage_parameter_ref:
    :ivar type_of_concession_ref:
    :ivar type_of_sales_offer_package_ref:
    :ivar type_of_travel_document_ref:
    :ivar type_of_machine_readability_ref:
    :ivar
        distribution_channel_ref_or_group_of_distribution_channels_ref:
    :ivar fulfilment_method_ref:
    :ivar type_of_payment_method_ref:
    """

    class Meta:
        name = "validityParameters_RelStructure"

    vehicle_modes: List[List[VehicleModeEnumeration]] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
            "tokens": True,
        },
    )
    transport_submode: List[TransportSubmode] = field(
        default_factory=list,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    group_of_operators_ref: List[GroupOfOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    all_operators_ref_or_operator_ref: List[
        Union[AllOperatorsRef, OperatorRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllOperatorsRef",
                    "type": AllOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    all_authorities_ref_or_authority_ref: List[
        Union[AllAuthoritiesRef, AuthorityRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllAuthoritiesRef",
                    "type": AllAuthoritiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    network_ref_or_group_of_lines_ref: List[
        Union[NetworkRef, GroupOfLinesRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    flexible_line_ref_or_line_ref: List[Union[FlexibleLineRef, LineRef]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "FlexibleLineRef",
                        "type": FlexibleLineRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "LineRef",
                        "type": LineRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    type_of_line_ref: List[TypeOfLineRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    tariff_zone_ref: List[TariffZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    fare_zone_ref: List[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    fare_section_ref: List[FareSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: List[
        Union[FareScheduledStopPointRef, ScheduledStopPointRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    place_use: List[PlaceUseEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PlaceUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    topographic_place_ref: List[TopographicPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    postal_address_ref_or_road_address_ref_or_address_ref: List[
        Union[PostalAddressRef, RoadAddressRef, AddressRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
    choice: List[
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
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
            SiteElementRef,
        ]
    ] = field(
        default_factory=list,
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
            ),
        },
    )
    point_of_interest_classification_ref: List[
        PointOfInterestClassificationRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    routing_type: List[RoutingTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RoutingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    directions: List[RelativeDirectionEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Directions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    series_constraint_ref: List[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    class_of_use_ref: List[ClassOfUseRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    fare_class: List[FareClass] = field(
        default_factory=list,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref: List[
        Union[ServiceFacilitySetRef, SiteFacilitySetRef, FacilitySetRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilitySetRef",
                    "type": FacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_product_category_ref: List[TypeOfProductCategoryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    template_service_journey_ref_or_service_journey_ref: List[
        Union[TemplateServiceJourneyRef, ServiceJourneyRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_number_ref: List[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    group_of_services_ref: List[GroupOfServicesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServicesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: List[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_service_ref: List[TypeOfServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    train_element_ref: List[TrainElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    train_component_label_assignment_ref: List[
        TrainComponentLabelAssignmentRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    passenger_seat_ref: List[PassengerSeatRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_fare_structure_factor_ref: List[TypeOfFareStructureFactorRef] = (
        field(
            default_factory=list,
            metadata={
                "name": "TypeOfFareStructureFactorRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequence": 1,
            },
        )
    )
    type_of_fare_structure_element_ref: List[TypeOfFareStructureElementRef] = (
        field(
            default_factory=list,
            metadata={
                "name": "TypeOfFareStructureElementRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "sequence": 1,
            },
        )
    )
    type_of_tariff_ref: List[TypeOfTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref: List[
        Union[LimitingRuleRef, DiscountingRuleRef, PricingRuleRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_pricing_rule_ref: List[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    charging_moment_ref: List[ChargingMomentRef] = field(
        default_factory=list,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_fare_product_ref: List[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_usage_parameter_ref: List[TypeOfUsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_concession_ref: List[TypeOfConcessionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_sales_offer_package_ref: List[TypeOfSalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_travel_document_ref: List[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_machine_readability_ref: List[TypeOfMachineReadabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    distribution_channel_ref_or_group_of_distribution_channels_ref: List[
        Union[DistributionChannelRef, GroupOfDistributionChannelsRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    fulfilment_method_ref: List[FulfilmentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_payment_method_ref: List[TypeOfPaymentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
