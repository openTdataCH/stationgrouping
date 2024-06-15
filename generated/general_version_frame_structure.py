from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDateTime

from generated.access import Access
from generated.access_equipment import AccessEquipment
from generated.access_right_in_product import AccessRightInProduct
from generated.access_right_parameter_assignment import (
    AccessRightParameterAssignment,
)
from generated.access_space import AccessSpace
from generated.access_vehicle_equipment import AccessVehicleEquipment
from generated.access_zone import AccessZone
from generated.accessibility_assessment import AccessibilityAssessment
from generated.accommodation import Accommodation
from generated.accountable_element import AccountableElement
from generated.activation_assignment import ActivationAssignment
from generated.activation_link import ActivationLink
from generated.activation_point import ActivationPoint
from generated.addressable_place import AddressablePlace
from generated.administrative_zones_rel_structure import (
    AdministrativeZone,
    TransportAdministrativeZone,
)
from generated.allowed_line_direction import AllowedLineDirection
from generated.alternative_name import AlternativeName
from generated.amount_of_price_unit_product import AmountOfPriceUnitProduct
from generated.assistance_booking_service import AssistanceBookingService
from generated.assistance_service import AssistanceService
from generated.authority import Authority
from generated.beacon_point import BeaconPoint
from generated.blacklist import Blacklist
from generated.block import Block
from generated.block_part import BlockPart
from generated.boarding_position import BoardingPosition
from generated.border_point import BorderPoint
from generated.branding import Branding
from generated.cancelling import Cancelling
from generated.capped_discount_right import CappedDiscountRight
from generated.capping_rule import CappingRule
from generated.capping_rule_price import CappingRulePrice
from generated.catering_service import CateringService
from generated.charging_moment import ChargingMoment
from generated.charging_policy import ChargingPolicy
from generated.check_constraint import CheckConstraint
from generated.check_constraint_delay import CheckConstraintDelay
from generated.check_constraint_throughput import CheckConstraintThroughput
from generated.class_of_use import ClassOfUse
from generated.codespace_assignment import CodespaceAssignment
from generated.commercial_profile import CommercialProfile
from generated.commercial_profile_eligibility import (
    CommercialProfileEligibility,
)
from generated.common_version_frame_structure import (
    CommonVersionFrameStructure,
)
from generated.communication_service import CommunicationService
from generated.companion_profile import CompanionProfile
from generated.complaints_service import ComplaintsService
from generated.complex_feature_projection import ComplexFeatureProjection
from generated.compound_block import CompoundBlock
from generated.compound_train import CompoundTrain
from generated.connection import Connection
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.control_centre import ControlCentre
from generated.controllable_element import ControllableElement
from generated.controllable_element_in_sequence import (
    ControllableElementInSequence,
)
from generated.controllable_element_price import ControllableElementPrice
from generated.country import Country
from generated.coupled_journey import CoupledJourney
from generated.course_of_journeys import CourseOfJourneys
from generated.crew_base import CrewBase
from generated.crossing_equipment import CrossingEquipment
from generated.customer import Customer
from generated.customer_account import CustomerAccount
from generated.customer_account_security_listing import (
    CustomerAccountSecurityListing,
)
from generated.customer_account_status import CustomerAccountStatus
from generated.customer_eligibility import CustomerEligibility
from generated.customer_purchase_package import CustomerPurchasePackage
from generated.customer_purchase_package_element import (
    CustomerPurchasePackageElement,
)
from generated.customer_purchase_package_price import (
    CustomerPurchasePackagePrice,
)
from generated.customer_purchase_parameter_assignment import (
    CustomerPurchaseParameterAssignment,
)
from generated.customer_security_listing import CustomerSecurityListing
from generated.customer_service import CustomerService
from generated.cycle_storage_equipment import CycleStorageEquipment
from generated.data_source import DataSource
from generated.dated_passing_time import DatedPassingTime
from generated.dated_service_journey import DatedServiceJourney
from generated.dated_special_service import DatedSpecialService
from generated.dated_vehicle_journey import DatedVehicleJourney
from generated.day_type_assignment import DayTypeAssignment
from generated.dead_run import DeadRun
from generated.dead_run_journey_pattern import DeadRunJourneyPattern
from generated.default_connection import DefaultConnection
from generated.default_dead_run_run_time import DefaultDeadRunRunTime
from generated.default_interchange import DefaultInterchange
from generated.default_service_journey_run_time import (
    DefaultServiceJourneyRunTime,
)
from generated.delivery_variant import DeliveryVariant
from generated.department import Department
from generated.destination_display import DestinationDisplay
from generated.destination_display_variant import DestinationDisplayVariant
from generated.direction import Direction
from generated.discounting_rule import DiscountingRule
from generated.display_assignment import DisplayAssignment
from generated.distance_matrix_element import DistanceMatrixElement
from generated.distance_matrix_element_price import DistanceMatrixElementPrice
from generated.distribution_assignment import DistributionAssignment
from generated.distribution_channel import DistributionChannel
from generated.driver_schedule_frame import DriverScheduleFrame
from generated.driver_trip import DriverTrip
from generated.driver_trip_time import DriverTripTime
from generated.duty import Duty
from generated.duty_part import DutyPart
from generated.dynamic_stop_assignment import DynamicStopAssignment
from generated.eligibility_change_policy import EligibilityChangePolicy
from generated.entitlement_given import EntitlementGiven
from generated.entitlement_product import EntitlementProduct
from generated.entitlement_required import EntitlementRequired
from generated.entity_in_version_structure import (
    AlternativeText,
    AvailabilityCondition,
    DayType,
    FareDayType,
    OperatingDay,
    OrganisationDayType,
    SimpleAvailabilityCondition,
    ValidDuring,
    ValidityCondition,
    ValidityRuleParameter,
    ValidityTrigger,
)
from generated.entity_structure import EntityStructure
from generated.entrance import Entrance
from generated.entrance_equipment import EntranceEquipment
from generated.equipment_place import EquipmentPlace
from generated.equipment_position import EquipmentPosition
from generated.escalator_equipment import EscalatorEquipment
from generated.estimated_passing_time import EstimatedPassingTime
from generated.exchanging import Exchanging
from generated.facility_requirement import FacilityRequirement
from generated.fare_contract import FareContract
from generated.fare_contract_entry import FareContractEntry
from generated.fare_contract_security_listing import (
    FareContractSecurityListing,
)
from generated.fare_demand_factor import FareDemandFactor
from generated.fare_element_in_sequence import FareElementInSequence
from generated.fare_frame import FareFrame
from generated.fare_interval import FareInterval
from generated.fare_point_in_pattern import FarePointInPattern
from generated.fare_product_price import FareProductPrice
from generated.fare_quota_factor import FareQuotaFactor
from generated.fare_scheduled_stop_point import FareScheduledStopPoint
from generated.fare_structure_element import FareStructureElement
from generated.fare_structure_element_in_sequence import (
    FareStructureElementInSequence,
)
from generated.fare_structure_element_price import FareStructureElementPrice
from generated.fare_structure_factor import FareStructureFactor
from generated.fare_unit import FareUnit
from generated.fare_zone import FareZone
from generated.flexible_area import FlexibleArea
from generated.flexible_line import FlexibleLine
from generated.flexible_link_properties import FlexibleLinkProperties
from generated.flexible_point_properties import FlexiblePointProperties
from generated.flexible_quay import FlexibleQuay
from generated.flexible_route import FlexibleRoute
from generated.flexible_service_properties import FlexibleServiceProperties
from generated.flexible_stop_assignment import FlexibleStopAssignment
from generated.flexible_stop_place import FlexibleStopPlace
from generated.frequency_of_use import FrequencyOfUse
from generated.fulfilment_method import FulfilmentMethod
from generated.fulfilment_method_price import FulfilmentMethodPrice
from generated.garage import Garage
from generated.garage_point import GaragePoint
from generated.general_frame_member import GeneralFrameMember
from generated.general_group_of_entities import GeneralGroupOfEntities
from generated.general_organisation import GeneralOrganisation
from generated.general_sign import GeneralSign
from generated.general_zone import GeneralZone
from generated.generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from generated.geographical_interval import GeographicalInterval
from generated.geographical_interval_price import GeographicalIntervalPrice
from generated.geographical_structure_factor import GeographicalStructureFactor
from generated.geographical_unit import GeographicalUnit
from generated.geographical_unit_price import GeographicalUnitPrice
from generated.group_constraint_member import GroupConstraintMember
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
from generated.group_of_sales_offer_packages import GroupOfSalesOfferPackages
from generated.group_of_services import GroupOfServices
from generated.group_of_timebands import GroupOfTimebands
from generated.group_of_timing_links import GroupOfTimingLinks
from generated.group_ticket import GroupTicket
from generated.hail_and_ride_area import HailAndRideArea
from generated.heading_sign import HeadingSign
from generated.headway_journey_group import HeadwayJourneyGroup
from generated.help_point_equipment import HelpPointEquipment
from generated.hire_service import HireService
from generated.infrastructure_frame import InfrastructureFrame
from generated.interchange_rule import InterchangeRule
from generated.interchange_rule_timing import InterchangeRuleTiming
from generated.interchanging import Interchanging
from generated.journey_accounting import JourneyAccounting
from generated.journey_headway import JourneyHeadway
from generated.journey_layover import JourneyLayover
from generated.journey_meeting import JourneyMeeting
from generated.journey_part import JourneyPart
from generated.journey_part_couple import JourneyPartCouple
from generated.journey_part_position import JourneyPartPosition
from generated.journey_pattern_headway import JourneyPatternHeadway
from generated.journey_pattern_layover import JourneyPatternLayover
from generated.journey_pattern_run_time import JourneyPatternRunTime
from generated.journey_pattern_wait_time import JourneyPatternWaitTime
from generated.journey_run_time import JourneyRunTime
from generated.journey_wait_time import JourneyWaitTime
from generated.layer import Layer
from generated.left_luggage_service import LeftLuggageService
from generated.level import Level
from generated.lift_equipment import LiftEquipment
from generated.limiting_rule import LimitingRule
from generated.limiting_rule_in_context import LimitingRuleInContext
from generated.line import Line
from generated.line_network import LineNetwork
from generated.line_shape import LineShape
from generated.link_in_journey_pattern import LinkInJourneyPattern
from generated.link_on_section import LinkOnSection
from generated.link_projection import LinkProjection
from generated.link_sequence_projection import LinkSequenceProjection
from generated.logical_display import LogicalDisplay
from generated.lost_property_service import LostPropertyService
from generated.luggage_allowance import LuggageAllowance
from generated.luggage_service import LuggageService
from generated.management_agent import ManagementAgent
from generated.meeting_point_service import MeetingPointService
from generated.meeting_restriction import MeetingRestriction
from generated.minimum_stay import MinimumStay
from generated.money_service import MoneyService
from generated.month_validity_offset import MonthValidityOffset
from generated.navigation_path import NavigationPath
from generated.navigation_path_assignment import NavigationPathAssignment
from generated.network import Network
from generated.normal_dated_vehicle_journey import NormalDatedVehicleJourney
from generated.notice import Notice
from generated.notice_assignment import NoticeAssignment
from generated.observed_passing_time import ObservedPassingTime
from generated.offered_travel_specification import OfferedTravelSpecification
from generated.onboard_stay import OnboardStay
from generated.open_transport_mode import OpenTransportMode
from generated.operating_department import OperatingDepartment
from generated.operating_period import OperatingPeriod
from generated.operational_context import OperationalContext
from generated.operator import Operator
from generated.organisation_part import OrganisationPart
from generated.organisational_unit import OrganisationalUnit
from generated.other_organisation import OtherOrganisation
from generated.overtaking_possibility import OvertakingPossibility
from generated.parking import Parking
from generated.parking_area import ParkingArea
from generated.parking_bay import ParkingBay
from generated.parking_capacity import ParkingCapacity
from generated.parking_component import ParkingComponent
from generated.parking_entrance_for_vehicles import ParkingEntranceForVehicles
from generated.parking_passenger_entrance import ParkingPassengerEntrance
from generated.parking_point import ParkingPoint
from generated.parking_properties import ParkingProperties
from generated.parking_tariff import ParkingTariff
from generated.passenger_carrying_requirement import (
    PassengerCarryingRequirement,
)
from generated.passenger_carrying_requirements_view import (
    PassengerCarryingRequirementsView,
)
from generated.passenger_information_equipment import (
    PassengerInformationEquipment,
)
from generated.passenger_safety_equipment import PassengerSafetyEquipment
from generated.passenger_stop_assignment import PassengerStopAssignment
from generated.passing_time import PassingTime
from generated.passing_time_view import PassingTimeView
from generated.path_junction import PathJunction
from generated.path_link import PathLink
from generated.path_link_in_sequence import PathLinkInSequence
from generated.penalty_policy import PenaltyPolicy
from generated.place_in_sequence import PlaceInSequence
from generated.place_lighting import PlaceLighting
from generated.place_sign import PlaceSign
from generated.point_2 import Point2
from generated.point_in_journey_pattern import PointInJourneyPattern
from generated.point_of_interest import PointOfInterest
from generated.point_of_interest_classification import (
    PointOfInterestClassification,
)
from generated.point_of_interest_classification_hierarchy import (
    PointOfInterestClassificationHierarchy,
)
from generated.point_of_interest_entrance import PointOfInterestEntrance
from generated.point_of_interest_space import PointOfInterestSpace
from generated.point_of_interest_vehicle_entrance import (
    PointOfInterestVehicleEntrance,
)
from generated.point_on_line_section import PointOnLineSection
from generated.point_on_link import PointOnLink
from generated.point_on_route import PointOnRoute
from generated.point_on_section import PointOnSection
from generated.point_projection import PointProjection
from generated.postal_address import PostalAddress
from generated.preassigned_fare_product import PreassignedFareProduct
from generated.price_unit import PriceUnit
from generated.priceable_object_version_structure import (
    Cell,
    FareTable,
    FareTableInContext,
    ParkingChargeBand,
    ParkingPrice,
    PriceGroup,
)
from generated.pricing_parameter_set import PricingParameterSet
from generated.pricing_rule import PricingRule
from generated.pricing_service import PricingService
from generated.purchase_window import PurchaseWindow
from generated.purpose_of_equipment_profile import PurposeOfEquipmentProfile
from generated.purpose_of_grouping import PurposeOfGrouping
from generated.purpose_of_journey_partition import PurposeOfJourneyPartition
from generated.quality_structure_factor import QualityStructureFactor
from generated.quality_structure_factor_price import (
    QualityStructureFactorPrice,
)
from generated.quay import Quay
from generated.queueing_equipment import QueueingEquipment
from generated.railway_element import RailwayElement
from generated.railway_junction import RailwayJunction
from generated.ramp_equipment import RampEquipment
from generated.refunding import Refunding
from generated.relief_opportunity import ReliefOpportunity
from generated.relief_point import ReliefPoint
from generated.replacing import Replacing
from generated.requested_travel_specification import (
    RequestedTravelSpecification,
)
from generated.reselling import Reselling
from generated.reserving import Reserving
from generated.residential_qualification import ResidentialQualification
from generated.residential_qualification_eligibility import (
    ResidentialQualificationEligibility,
)
from generated.resource_frame import ResourceFrame
from generated.responsibility_set import ResponsibilitySet
from generated.restricted_manoeuvre import RestrictedManoeuvre
from generated.retail_consortium import RetailConsortium
from generated.retail_device import RetailDevice
from generated.retail_device_security_listing import (
    RetailDeviceSecurityListing,
)
from generated.retail_service import RetailService
from generated.rhythmical_journey_group import RhythmicalJourneyGroup
from generated.road_address import RoadAddress
from generated.road_element import RoadElement
from generated.road_junction import RoadJunction
from generated.rough_surface import RoughSurface
from generated.round_trip import RoundTrip
from generated.rounding import Rounding
from generated.route import Route
from generated.route_instruction import RouteInstruction
from generated.route_link import RouteLink
from generated.route_point import RoutePoint
from generated.routing import Routing
from generated.routing_constraint_zone import RoutingConstraintZone
from generated.rubbish_disposal_equipment import RubbishDisposalEquipment
from generated.sale_discount_right import SaleDiscountRight
from generated.sales_notice_assignment import SalesNoticeAssignment
from generated.sales_offer_package import SalesOfferPackage
from generated.sales_offer_package_element import SalesOfferPackageElement
from generated.sales_offer_package_entitlement_given import (
    SalesOfferPackageEntitlementGiven,
)
from generated.sales_offer_package_entitlement_required import (
    SalesOfferPackageEntitlementRequired,
)
from generated.sales_offer_package_price import SalesOfferPackagePrice
from generated.sales_offer_package_substitution import (
    SalesOfferPackageSubstitution,
)
from generated.sales_transaction import SalesTransaction
from generated.sales_transaction_frame import SalesTransactionFrame
from generated.sanitary_equipment import SanitaryEquipment
from generated.scheduled_stop_point import ScheduledStopPoint
from generated.schematic_map import SchematicMap
from generated.seating_equipment import SeatingEquipment
from generated.sections_in_sequence_rel_structure import (
    JourneyPattern,
    SectionInSequence,
)
from generated.series_constraint import SeriesConstraint
from generated.series_constraint_price import SeriesConstraintPrice
from generated.service_access_right_1 import ServiceAccessRight1
from generated.service_access_right_2 import ServiceAccessRight2
from generated.service_calendar import ServiceCalendar
from generated.service_calendar_frame import ServiceCalendarFrame
from generated.service_exclusion import ServiceExclusion
from generated.service_frame import ServiceFrame
from generated.service_journey import ServiceJourney
from generated.service_journey_interchange import ServiceJourneyInterchange
from generated.service_journey_pattern import ServiceJourneyPattern
from generated.service_journey_pattern_interchange import (
    ServiceJourneyPatternInterchange,
)
from generated.service_link import ServiceLink
from generated.service_link_in_journey_pattern import (
    ServiceLinkInJourneyPattern,
)
from generated.service_pattern import ServicePattern
from generated.service_site import ServiceSite
from generated.serviced_organisation import ServicedOrganisation
from generated.shelter_equipment import ShelterEquipment
from generated.sign_equipment import SignEquipment
from generated.site_connection import SiteConnection
from generated.site_frame import SiteFrame
from generated.site_path_link import SitePathLink
from generated.special_service import SpecialService
from generated.specific_parameter_assignments_rel_structure import (
    SpecificParameterAssignment,
)
from generated.stair_flight import StairFlight
from generated.staircase_equipment import StaircaseEquipment
from generated.standard_fare_table import StandardFareTable
from generated.start_time_at_stop_point import StartTimeAtStopPoint
from generated.step_limit import StepLimit
from generated.stop_area import StopArea
from generated.stop_place import StopPlace
from generated.stop_place_entrance import StopPlaceEntrance
from generated.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from generated.stop_point_in_journey_pattern import StopPointInJourneyPattern
from generated.submode import Submode
from generated.subscribing import Subscribing
from generated.supplement_product import SupplementProduct
from generated.suspending import Suspending
from generated.target_passing_time import TargetPassingTime
from generated.tariff import Tariff
from generated.tariff_zone import TariffZone
from generated.template_service_journey import TemplateServiceJourney
from generated.template_vehicle_journey import TemplateVehicleJourney
from generated.third_party_product import ThirdPartyProduct
from generated.ticket_validator_equipment import TicketValidatorEquipment
from generated.ticketing_equipment import TicketingEquipment
from generated.ticketing_service import TicketingService
from generated.time_demand_profile import TimeDemandProfile
from generated.time_demand_profile_member import TimeDemandProfileMember
from generated.time_demand_type import TimeDemandType
from generated.time_demand_type_assignment import TimeDemandTypeAssignment
from generated.time_interval import TimeInterval
from generated.time_interval_price import TimeIntervalPrice
from generated.time_structure_factor import TimeStructureFactor
from generated.time_unit import TimeUnit
from generated.time_unit_price import TimeUnitPrice
from generated.timeband import Timeband
from generated.timetable_frame import TimetableFrame
from generated.timetabled_passing_time import TimetabledPassingTime
from generated.timing_algorithm_type import TimingAlgorithmType
from generated.timing_link import TimingLink
from generated.timing_link_in_journey_pattern import TimingLinkInJourneyPattern
from generated.timing_pattern import TimingPattern
from generated.timing_point import TimingPoint
from generated.timing_point_in_journey_pattern import (
    TimingPointInJourneyPattern,
)
from generated.topographic_place import TopographicPlace
from generated.topographic_projection import TopographicProjection
from generated.traffic_control_point import TrafficControlPoint
from generated.train import Train
from generated.train_block import TrainBlock
from generated.train_block_part import TrainBlockPart
from generated.train_component import TrainComponent
from generated.train_component_label_assignment import (
    TrainComponentLabelAssignment,
)
from generated.train_element import TrainElement
from generated.train_number import TrainNumber
from generated.train_stop_assignment import TrainStopAssignment
from generated.transfer_restriction import TransferRestriction
from generated.transferability import Transferability
from generated.travel_agent import TravelAgent
from generated.travel_document import TravelDocument
from generated.travel_document_security_listing import (
    TravelDocumentSecurityListing,
)
from generated.travel_specification_1 import TravelSpecification1
from generated.travel_specification_2 import TravelSpecification2
from generated.travelator_equipment import TravelatorEquipment
from generated.trolley_stand_equipment import TrolleyStandEquipment
from generated.turnaround_time_limit_time import TurnaroundTimeLimitTime
from generated.type_of_access_right_assignment import (
    TypeOfAccessRightAssignment,
)
from generated.type_of_activation import TypeOfActivation
from generated.type_of_codespace_assignment import TypeOfCodespaceAssignment
from generated.type_of_concession import TypeOfConcession
from generated.type_of_congestion import TypeOfCongestion
from generated.type_of_customer_account import TypeOfCustomerAccount
from generated.type_of_delivery_variant import TypeOfDeliveryVariant
from generated.type_of_entity import TypeOfEntity
from generated.type_of_equipment import TypeOfEquipment
from generated.type_of_facility import TypeOfFacility
from generated.type_of_fare_contract import TypeOfFareContract
from generated.type_of_fare_contract_entry import TypeOfFareContractEntry
from generated.type_of_fare_product import TypeOfFareProduct
from generated.type_of_fare_structure_element import TypeOfFareStructureElement
from generated.type_of_fare_structure_factor import TypeOfFareStructureFactor
from generated.type_of_fare_table import TypeOfFareTable
from generated.type_of_feature import TypeOfFeature
from generated.type_of_flexible_service import TypeOfFlexibleService
from generated.type_of_journey_pattern import TypeOfJourneyPattern
from generated.type_of_line import TypeOfLine
from generated.type_of_link import TypeOfLink
from generated.type_of_link_sequence import TypeOfLinkSequence
from generated.type_of_machine_readability import TypeOfMachineReadability
from generated.type_of_notice import TypeOfNotice
from generated.type_of_operation import TypeOfOperation
from generated.type_of_organisation import TypeOfOrganisation
from generated.type_of_organisation_part import TypeOfOrganisationPart
from generated.type_of_passenger_information_equipment import (
    TypeOfPassengerInformationEquipment,
)
from generated.type_of_payment_method import TypeOfPaymentMethod
from generated.type_of_place import TypeOfPlace
from generated.type_of_point import TypeOfPoint
from generated.type_of_pricing_rule import TypeOfPricingRule
from generated.type_of_product_category import TypeOfProductCategory
from generated.type_of_projection import TypeOfProjection
from generated.type_of_responsibility_role import TypeOfResponsibilityRole
from generated.type_of_retail_device import TypeOfRetailDevice
from generated.type_of_sales_offer_package import TypeOfSalesOfferPackage
from generated.type_of_security_list import TypeOfSecurityList
from generated.type_of_service import TypeOfService
from generated.type_of_service_feature import TypeOfServiceFeature
from generated.type_of_tariff import TypeOfTariff
from generated.type_of_time_demand_type import TypeOfTimeDemandType
from generated.type_of_transfer import TypeOfTransfer
from generated.type_of_travel_document import TypeOfTravelDocument
from generated.type_of_usage_parameter import TypeOfUsageParameter
from generated.type_of_validity import TypeOfValidity
from generated.type_of_version import TypeOfVersion
from generated.type_of_zone import TypeOfZone
from generated.types_of_frame_rel_structure import TypeOfFrame
from generated.uic_operating_period import UicOperatingPeriod
from generated.usage_discount_right import UsageDiscountRight
from generated.usage_parameter_price import UsageParameterPrice
from generated.usage_validity_period import UsageValidityPeriod
from generated.user_profile import UserProfile
from generated.user_profile_eligibility import UserProfileEligibility
from generated.validable_element import ValidableElement
from generated.validable_element_price import ValidableElementPrice
from generated.validity_parameter_assignment import ValidityParameterAssignment
from generated.value_set import ValueSet
from generated.vehicle import Vehicle
from generated.vehicle_charging_equipment import VehicleChargingEquipment
from generated.vehicle_equipment_profile import VehicleEquipmentProfile
from generated.vehicle_journey import VehicleJourney
from generated.vehicle_journey_headway import VehicleJourneyHeadway
from generated.vehicle_journey_layover import VehicleJourneyLayover
from generated.vehicle_journey_run_time import VehicleJourneyRunTime
from generated.vehicle_journey_stop_assignment import (
    VehicleJourneyStopAssignment,
)
from generated.vehicle_journey_wait_time import VehicleJourneyWaitTime
from generated.vehicle_manoeuvring_requirement import (
    VehicleManoeuvringRequirement,
)
from generated.vehicle_model import VehicleModel
from generated.vehicle_position_alignment import VehiclePositionAlignment
from generated.vehicle_quay_alignment import VehicleQuayAlignment
from generated.vehicle_schedule_frame import VehicleScheduleFrame
from generated.vehicle_service import VehicleService
from generated.vehicle_service_part import VehicleServicePart
from generated.vehicle_stopping_place import VehicleStoppingPlace
from generated.vehicle_stopping_position import VehicleStoppingPosition
from generated.vehicle_type import VehicleType
from generated.vehicle_type_at_point import VehicleTypeAtPoint
from generated.vehicle_type_preference import VehicleTypePreference
from generated.vehicle_type_stop_assignment import VehicleTypeStopAssignment
from generated.version import Version
from generated.waiting_room_equipment import WaitingRoomEquipment
from generated.wheelchair_vehicle_equipment import WheelchairVehicleEquipment
from generated.whitelist import Whitelist
from generated.wire_element import WireElement
from generated.wire_junction import WireJunction
from generated.zone import Zone
from generated.zone_projection import ZoneProjection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a GENERAL FRAME.

    :ivar members: Entities in GENERAL FRAME.
    """

    class Meta:
        name = "General_VersionFrameStructure"

    members: Optional["GeneralFrameMembersRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class EntitiesInVersionRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in ENTITY of ENTITY In VERSION.
    """

    class Meta:
        name = "entitiesInVersion_RelStructure"

    choice: List[
        Union[
            ResidentialQualificationEligibility,
            CommercialProfileEligibility,
            UserProfileEligibility,
            CustomerEligibility,
            ResidentialQualification,
            AccessRightInProduct,
            FareStructureElementInSequence,
            StartTimeAtStopPoint,
            ControllableElementInSequence,
            FareElementInSequence,
            Cell,
            CustomerPurchasePackagePrice,
            ParkingPrice,
            SalesOfferPackagePrice,
            FulfilmentMethodPrice,
            CappingRulePrice,
            FareProductPrice,
            FareStructureElementPrice,
            TimeIntervalPrice,
            TimeUnitPrice,
            QualityStructureFactorPrice,
            ControllableElementPrice,
            ValidableElementPrice,
            UsageParameterPrice,
            DistanceMatrixElementPrice,
            GeographicalIntervalPrice,
            GeographicalUnitPrice,
            SeriesConstraintPrice,
            DefaultDeadRunRunTime,
            DefaultServiceJourneyRunTime,
            TimeDemandProfileMember,
            JourneyPartPosition,
            EstimatedPassingTime,
            ObservedPassingTime,
            TargetPassingTime,
            DatedPassingTime,
            TimetabledPassingTime,
            PassingTime,
            InterchangeRuleTiming,
            ParkingCapacity,
            ParkingProperties,
            VehicleTypePreference,
            VehiclePositionAlignment,
            VehicleQuayAlignment,
            StairFlight,
            FlexiblePointProperties,
            FlexibleLinkProperties,
            JourneyPatternHeadway,
            JourneyPatternLayover,
            JourneyPatternRunTime,
            JourneyPatternWaitTime,
            TurnaroundTimeLimitTime,
            VehicleJourneyLayover,
            VehicleJourneyRunTime,
            VehicleJourneyWaitTime,
            VehicleJourneyHeadway,
            JourneyHeadway,
            JourneyLayover,
            JourneyRunTime,
            JourneyWaitTime,
            TravelDocumentSecurityListing,
            RetailDeviceSecurityListing,
            FareContractSecurityListing,
            CustomerSecurityListing,
            CustomerAccountSecurityListing,
            OnboardStay,
            Accommodation,
            ServiceLinkInJourneyPattern,
            PathLinkInSequence,
            LinkInJourneyPattern,
            TimingLinkInJourneyPattern,
            FarePointInPattern,
            StopPointInJourneyPattern,
            PlaceInSequence,
            PointInJourneyPattern,
            PointOnRoute,
            TimingPointInJourneyPattern,
            PointOnLineSection,
            PointOnSection,
            SectionInSequence,
            LinkOnSection,
            CodespaceAssignment,
            PointOnLink,
            AccessibilityAssessment,
            AlternativeName,
            GroupConstraintMember,
            AlternativeText,
            TravelDocument,
            CustomerAccount,
            SalesTransaction,
            OfferedTravelSpecification,
            RequestedTravelSpecification,
            TravelSpecification1,
            TravelSpecification2,
            FareContractEntry,
            FareContract,
            Customer,
            ParkingTariff,
            GroupOfSalesOfferPackages,
            DistributionChannel,
            Tariff,
            CustomerPurchasePackage,
            SalesOfferPackage,
            FulfilmentMethod,
            CappingRule,
            EntitlementProduct,
            SupplementProduct,
            PreassignedFareProduct,
            AmountOfPriceUnitProduct,
            CappedDiscountRight,
            UsageDiscountRight,
            ThirdPartyProduct,
            SaleDiscountRight,
            ServiceAccessRight1,
            ServiceAccessRight2,
            TimeInterval,
            FareQuotaFactor,
            FareDemandFactor,
            QualityStructureFactor,
            ControllableElement,
            ValidableElement,
            SalesOfferPackageEntitlementRequired,
            SalesOfferPackageEntitlementGiven,
            MinimumStay,
            Interchanging,
            Suspending,
            UsageValidityPeriod,
            FrequencyOfUse,
            StepLimit,
            Routing,
            RoundTrip,
            LuggageAllowance,
            EntitlementRequired,
            EntitlementGiven,
            EligibilityChangePolicy,
            CompanionProfile,
            GroupTicket,
            CommercialProfile,
            UserProfile,
            Subscribing,
            PenaltyPolicy,
            ChargingPolicy,
            Cancelling,
            Reserving,
            PurchaseWindow,
            Transferability,
            Replacing,
            Refunding,
            Exchanging,
            Reselling,
            GeographicalInterval,
            SeriesConstraint,
            CustomerPurchasePackageElement,
            ParkingChargeBand,
            SalesOfferPackageElement,
            FareStructureElement,
            TimeStructureFactor,
            TimeUnit,
            DistanceMatrixElement,
            GeographicalStructureFactor,
            GeographicalUnit,
            FareUnit,
            FareInterval,
            FareStructureFactor,
            PricingService,
            LimitingRuleInContext,
            LimitingRule,
            DiscountingRule,
            PricingRule,
            MonthValidityOffset,
            Rounding,
            PricingParameterSet,
            ReliefOpportunity,
            CourseOfJourneys,
            VehicleServicePart,
            VehicleService,
            TrainBlockPart,
            CompoundBlock,
            BlockPart,
            TrainBlock,
            Block,
            DriverTripTime,
            DriverTrip,
            DutyPart,
            AccountableElement,
            Duty,
            TimeDemandProfile,
            VehicleTypeStopAssignment,
            TrainComponentLabelAssignment,
            TrainNumber,
            DatedSpecialService,
            NormalDatedVehicleJourney,
            DatedVehicleJourney,
            SpecialService,
            DeadRun,
            ServiceJourney,
            DatedServiceJourney,
            TemplateServiceJourney,
            TemplateVehicleJourney,
            VehicleJourney,
            FlexibleServiceProperties,
            JourneyPartCouple,
            CoupledJourney,
            JourneyPart,
            InterchangeRule,
            ServiceJourneyPatternInterchange,
            ServiceJourneyInterchange,
            DefaultInterchange,
            JourneyMeeting,
            PointOfInterestClassificationHierarchy,
            TimeDemandType,
            VehicleJourneyStopAssignment,
            FlexibleStopAssignment,
            NavigationPathAssignment,
            TrainStopAssignment,
            DynamicStopAssignment,
            PassengerStopAssignment,
            LogicalDisplay,
            Level,
            LineNetwork,
            RouteInstruction,
            AllowedLineDirection,
            DestinationDisplayVariant,
            DestinationDisplay,
            FlexibleLine,
            Line,
            OperationalContext,
            TrainComponent,
            TrainElement,
            CompoundTrain,
            Train,
            VehicleEquipmentProfile,
            VehicleModel,
            Vehicle,
            PassengerCarryingRequirementsView,
            FacilityRequirement,
            VehicleManoeuvringRequirement,
            PassengerCarryingRequirement,
            VehicleType,
            Whitelist,
            Blacklist,
            SchematicMap,
            DeliveryVariant,
            Notice,
            EquipmentPosition,
            AssistanceBookingService,
            CateringService,
            RetailService,
            MoneyService,
            HireService,
            CommunicationService,
            MeetingPointService,
            LostPropertyService,
            LeftLuggageService,
            ComplaintsService,
            CustomerService,
            LuggageService,
            AssistanceService,
            TicketingService,
            RetailDevice,
            TicketValidatorEquipment,
            TicketingEquipment,
            SeatingEquipment,
            ShelterEquipment,
            TrolleyStandEquipment,
            WaitingRoomEquipment,
            CrossingEquipment,
            QueueingEquipment,
            EntranceEquipment,
            RampEquipment,
            LiftEquipment,
            TravelatorEquipment,
            StaircaseEquipment,
            EscalatorEquipment,
            PlaceLighting,
            RoughSurface,
            AccessEquipment,
            GeneralSign,
            HeadingSign,
            PlaceSign,
            SignEquipment,
            WheelchairVehicleEquipment,
            AccessVehicleEquipment,
            VehicleChargingEquipment,
            CycleStorageEquipment,
            PassengerInformationEquipment,
            RubbishDisposalEquipment,
            HelpPointEquipment,
            PassengerSafetyEquipment,
            SanitaryEquipment,
            ServicePattern,
            NavigationPath,
            ServiceJourneyPattern,
            DeadRunJourneyPattern,
            JourneyPattern,
            FlexibleRoute,
            Route,
            TimingPattern,
            Connection,
            DefaultConnection,
            SiteConnection,
            Access,
            ControlCentre,
            OperatingDepartment,
            OrganisationalUnit,
            Department,
            OrganisationPart,
            RetailConsortium,
            Authority,
            Operator,
            ServicedOrganisation,
            GeneralOrganisation,
            ManagementAgent,
            TravelAgent,
            OtherOrganisation,
            ServiceLink,
            SitePathLink,
            PathLink,
            RouteLink,
            TimingLink,
            WireElement,
            RoadElement,
            RailwayElement,
            ActivationLink,
            BorderPoint,
            FareScheduledStopPoint,
            ScheduledStopPoint,
            PathJunction,
            RoutePoint,
            ParkingPoint,
            GaragePoint,
            ReliefPoint,
            TimingPoint,
            WireJunction,
            RoadJunction,
            RailwayJunction,
            TrafficControlPoint,
            BeaconPoint,
            ActivationPoint,
            Point2,
            LineShape,
            TopographicProjection,
            ZoneProjection,
            ComplexFeatureProjection,
            LinkSequenceProjection,
            LinkProjection,
            PointProjection,
            "CompositeFrame",
            SalesTransactionFrame,
            FareFrame,
            DriverScheduleFrame,
            VehicleScheduleFrame,
            ServiceFrame,
            TimetableFrame,
            SiteFrame,
            InfrastructureFrame,
            "GeneralFrame",
            ResourceFrame,
            ServiceCalendarFrame,
            UicOperatingPeriod,
            OperatingPeriod,
            OperatingDay,
            ServiceCalendar,
            DistributionAssignment,
            SalesOfferPackageSubstitution,
            CustomerPurchaseParameterAssignment,
            SpecificParameterAssignment,
            GenericParameterAssignmentInContext,
            GenericParameterAssignment,
            ValidityParameterAssignment,
            AccessRightParameterAssignment,
            JourneyAccounting,
            TimeDemandTypeAssignment,
            TransferRestriction,
            ServiceExclusion,
            DisplayAssignment,
            CheckConstraintThroughput,
            CheckConstraintDelay,
            CheckConstraint,
            OvertakingPossibility,
            MeetingRestriction,
            RestrictedManoeuvre,
            VehicleTypeAtPoint,
            ActivationAssignment,
            SalesNoticeAssignment,
            NoticeAssignment,
            DayTypeAssignment,
            GroupOfTimebands,
            Timeband,
            FareDayType,
            OrganisationDayType,
            DayType,
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
            ResponsibilitySet,
            ValueSet,
            TypeOfMachineReadability,
            TypeOfConcession,
            ChargingMoment,
            TypeOfUsageParameter,
            TypeOfFareTable,
            TypeOfPricingRule,
            PriceUnit,
            TimingAlgorithmType,
            PurposeOfJourneyPartition,
            TypeOfServiceFeature,
            PointOfInterestClassification,
            Direction,
            PurposeOfEquipmentProfile,
            TypeOfSecurityList,
            TypeOfProductCategory,
            TypeOfPaymentMethod,
            ClassOfUse,
            Submode,
            OpenTransportMode,
            TypeOfCodespaceAssignment,
            TypeOfValidity,
            PurposeOfGrouping,
            Branding,
            DataSource,
            TypeOfRetailDevice,
            CustomerAccountStatus,
            TypeOfCustomerAccount,
            TypeOfFareContractEntry,
            TypeOfFareContract,
            TypeOfTravelDocument,
            TypeOfSalesOfferPackage,
            TypeOfFareProduct,
            TypeOfFareStructureElement,
            TypeOfTariff,
            TypeOfAccessRightAssignment,
            TypeOfFareStructureFactor,
            TypeOfFlexibleService,
            TypeOfTimeDemandType,
            TypeOfPassengerInformationEquipment,
            TypeOfCongestion,
            TypeOfJourneyPattern,
            TypeOfLine,
            TypeOfActivation,
            TypeOfDeliveryVariant,
            TypeOfNotice,
            TypeOfFacility,
            TypeOfService,
            TypeOfEquipment,
            TypeOfFeature,
            TypeOfLinkSequence,
            TypeOfPlace,
            TypeOfTransfer,
            TypeOfOperation,
            TypeOfOrganisationPart,
            TypeOfOrganisation,
            TypeOfZone,
            TypeOfLink,
            TypeOfPoint,
            TypeOfProjection,
            TypeOfFrame,
            TypeOfResponsibilityRole,
            TypeOfEntity,
            TypeOfVersion,
            PassingTimeView,
            SimpleAvailabilityCondition,
            ValidDuring,
            AvailabilityCondition,
            ValidityRuleParameter,
            ValidityTrigger,
            ValidityCondition,
            Version,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationEligibility",
                    "type": ResidentialQualificationEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibility",
                    "type": CommercialProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibility",
                    "type": UserProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerEligibility",
                    "type": CustomerEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResidentialQualification",
                    "type": ResidentialQualification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProduct",
                    "type": AccessRightInProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequence",
                    "type": FareStructureElementInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTimeAtStopPoint",
                    "type": StartTimeAtStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementInSequence",
                    "type": ControllableElementInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareElementInSequence",
                    "type": FareElementInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Cell",
                    "type": Cell,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": ParkingPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultDeadRunRunTime",
                    "type": DefaultDeadRunRunTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultServiceJourneyRunTime",
                    "type": DefaultServiceJourneyRunTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandProfileMember",
                    "type": TimeDemandProfileMember,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartPosition",
                    "type": JourneyPartPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EstimatedPassingTime",
                    "type": EstimatedPassingTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ObservedPassingTime",
                    "type": ObservedPassingTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TargetPassingTime",
                    "type": TargetPassingTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedPassingTime",
                    "type": DatedPassingTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetabledPassingTime",
                    "type": TimetabledPassingTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTime",
                    "type": PassingTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRuleTiming",
                    "type": InterchangeRuleTiming,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingCapacity",
                    "type": ParkingCapacity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingProperties",
                    "type": ParkingProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypePreference",
                    "type": VehicleTypePreference,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePositionAlignment",
                    "type": VehiclePositionAlignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleQuayAlignment",
                    "type": VehicleQuayAlignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StairFlight",
                    "type": StairFlight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexiblePointProperties",
                    "type": FlexiblePointProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLinkProperties",
                    "type": FlexibleLinkProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternHeadway",
                    "type": JourneyPatternHeadway,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternLayover",
                    "type": JourneyPatternLayover,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRunTime",
                    "type": JourneyPatternRunTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternWaitTime",
                    "type": JourneyPatternWaitTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TurnaroundTimeLimitTime",
                    "type": TurnaroundTimeLimitTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyLayover",
                    "type": VehicleJourneyLayover,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRunTime",
                    "type": VehicleJourneyRunTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyWaitTime",
                    "type": VehicleJourneyWaitTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyHeadway",
                    "type": VehicleJourneyHeadway,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyHeadway",
                    "type": JourneyHeadway,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyLayover",
                    "type": JourneyLayover,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyRunTime",
                    "type": JourneyRunTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyWaitTime",
                    "type": JourneyWaitTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentSecurityListing",
                    "type": TravelDocumentSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDeviceSecurityListing",
                    "type": RetailDeviceSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractSecurityListing",
                    "type": FareContractSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerSecurityListing",
                    "type": CustomerSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountSecurityListing",
                    "type": CustomerAccountSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnboardStay",
                    "type": OnboardStay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Accommodation",
                    "type": Accommodation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLinkInJourneyPattern",
                    "type": ServiceLinkInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkInSequence",
                    "type": PathLinkInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkInJourneyPattern",
                    "type": LinkInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkInJourneyPattern",
                    "type": TimingLinkInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePointInPattern",
                    "type": FarePointInPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPattern",
                    "type": StopPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceInSequence",
                    "type": PlaceInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPattern",
                    "type": PointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOnRoute",
                    "type": PointOnRoute,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPattern",
                    "type": TimingPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOnLineSection",
                    "type": PointOnLineSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOnSection",
                    "type": PointOnSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SectionInSequence",
                    "type": SectionInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkOnSection",
                    "type": LinkOnSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CodespaceAssignment",
                    "type": CodespaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOnLink",
                    "type": PointOnLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessibilityAssessment",
                    "type": AccessibilityAssessment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeName",
                    "type": AlternativeName,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupConstraintMember",
                    "type": GroupConstraintMember,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeText",
                    "type": AlternativeText,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocument",
                    "type": TravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccount",
                    "type": CustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransaction",
                    "type": SalesTransaction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecification",
                    "type": RequestedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification",
                    "type": TravelSpecification1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification_",
                    "type": TravelSpecification2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntry_",
                    "type": FareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContract",
                    "type": FareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Customer",
                    "type": Customer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingTariff",
                    "type": ParkingTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackages",
                    "type": GroupOfSalesOfferPackages,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannel",
                    "type": DistributionChannel,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Tariff",
                    "type": Tariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackage",
                    "type": CustomerPurchasePackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackage",
                    "type": SalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethod",
                    "type": FulfilmentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRule",
                    "type": CappingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementProduct",
                    "type": EntitlementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProduct",
                    "type": SupplementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProduct",
                    "type": PreassignedFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProduct",
                    "type": AmountOfPriceUnitProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRight",
                    "type": CappedDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRight",
                    "type": UsageDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProduct",
                    "type": ThirdPartyProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRight",
                    "type": SaleDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRight",
                    "type": ServiceAccessRight1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRight_",
                    "type": ServiceAccessRight2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeInterval",
                    "type": TimeInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactor",
                    "type": QualityStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElement",
                    "type": ControllableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElement",
                    "type": ValidableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequired",
                    "type": SalesOfferPackageEntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGiven",
                    "type": SalesOfferPackageEntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStay",
                    "type": MinimumStay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Interchanging",
                    "type": Interchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Suspending",
                    "type": Suspending,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriod",
                    "type": UsageValidityPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUse",
                    "type": FrequencyOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimit",
                    "type": StepLimit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Routing",
                    "type": Routing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTrip",
                    "type": RoundTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowance",
                    "type": LuggageAllowance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequired",
                    "type": EntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGiven",
                    "type": EntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicy",
                    "type": EligibilityChangePolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicket",
                    "type": GroupTicket,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfile",
                    "type": CommercialProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfile",
                    "type": UserProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Subscribing",
                    "type": Subscribing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicy",
                    "type": PenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicy",
                    "type": ChargingPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Cancelling",
                    "type": Cancelling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reserving",
                    "type": Reserving,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindow",
                    "type": PurchaseWindow,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Transferability",
                    "type": Transferability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Replacing",
                    "type": Replacing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Refunding",
                    "type": Refunding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Exchanging",
                    "type": Exchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reselling",
                    "type": Reselling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalInterval",
                    "type": GeographicalInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraint",
                    "type": SeriesConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElement",
                    "type": CustomerPurchasePackageElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBand",
                    "type": ParkingChargeBand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElement",
                    "type": SalesOfferPackageElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElement",
                    "type": FareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactor",
                    "type": TimeStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnit",
                    "type": TimeUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElement",
                    "type": DistanceMatrixElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactor",
                    "type": GeographicalStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnit",
                    "type": GeographicalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareUnit",
                    "type": FareUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareInterval",
                    "type": FareInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureFactor",
                    "type": FareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingService",
                    "type": PricingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRuleInContext",
                    "type": LimitingRuleInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRule",
                    "type": LimitingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRule",
                    "type": DiscountingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRule",
                    "type": PricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonthValidityOffset",
                    "type": MonthValidityOffset,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Rounding",
                    "type": Rounding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingParameterSet",
                    "type": PricingParameterSet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefOpportunity",
                    "type": ReliefOpportunity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CourseOfJourneys",
                    "type": CourseOfJourneys,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePart",
                    "type": VehicleServicePart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleService",
                    "type": VehicleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockPart",
                    "type": TrainBlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundBlock",
                    "type": CompoundBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPart",
                    "type": BlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlock",
                    "type": TrainBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Block",
                    "type": Block,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripTime",
                    "type": DriverTripTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTrip",
                    "type": DriverTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyPart",
                    "type": DutyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccountableElement",
                    "type": AccountableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Duty",
                    "type": Duty,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandProfile",
                    "type": TimeDemandProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeStopAssignment",
                    "type": VehicleTypeStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentLabelAssignment",
                    "type": TrainComponentLabelAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumber",
                    "type": TrainNumber,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialService",
                    "type": DatedSpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourney",
                    "type": NormalDatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourney",
                    "type": DatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRun",
                    "type": DeadRun,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourney",
                    "type": ServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedServiceJourney",
                    "type": DatedServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourney",
                    "type": TemplateServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateVehicleJourney",
                    "type": TemplateVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourney",
                    "type": VehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServiceProperties",
                    "type": FlexibleServiceProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartCouple",
                    "type": JourneyPartCouple,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoupledJourney",
                    "type": CoupledJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPart",
                    "type": JourneyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRule",
                    "type": InterchangeRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternInterchange",
                    "type": ServiceJourneyPatternInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchange",
                    "type": ServiceJourneyInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultInterchange",
                    "type": DefaultInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyMeeting",
                    "type": JourneyMeeting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassificationHierarchy",
                    "type": PointOfInterestClassificationHierarchy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandType",
                    "type": TimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopAssignment",
                    "type": FlexibleStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathAssignment",
                    "type": NavigationPathAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignment",
                    "type": DynamicStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignment",
                    "type": PassengerStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogicalDisplay",
                    "type": LogicalDisplay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Level",
                    "type": Level,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineNetwork",
                    "type": LineNetwork,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteInstruction",
                    "type": RouteInstruction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirection",
                    "type": AllowedLineDirection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayVariant",
                    "type": DestinationDisplayVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplay",
                    "type": DestinationDisplay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLine",
                    "type": FlexibleLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Line",
                    "type": Line,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperationalContext",
                    "type": OperationalContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponent",
                    "type": TrainComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrain",
                    "type": CompoundTrain,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfile",
                    "type": VehicleEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleModel",
                    "type": VehicleModel,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Vehicle",
                    "type": Vehicle,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementsView",
                    "type": PassengerCarryingRequirementsView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilityRequirement",
                    "type": FacilityRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleManoeuvringRequirement",
                    "type": VehicleManoeuvringRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirement",
                    "type": PassengerCarryingRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleType",
                    "type": VehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Whitelist",
                    "type": Whitelist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Blacklist",
                    "type": Blacklist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SchematicMap",
                    "type": SchematicMap,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeliveryVariant",
                    "type": DeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Notice",
                    "type": Notice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPosition",
                    "type": EquipmentPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingService",
                    "type": AssistanceBookingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringService",
                    "type": CateringService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailService",
                    "type": RetailService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyService",
                    "type": MoneyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireService",
                    "type": HireService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationService",
                    "type": CommunicationService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointService",
                    "type": MeetingPointService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyService",
                    "type": LostPropertyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageService",
                    "type": LeftLuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsService",
                    "type": ComplaintsService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerService",
                    "type": CustomerService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageService",
                    "type": LuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceService",
                    "type": AssistanceService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingService",
                    "type": TicketingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDevice",
                    "type": RetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipment",
                    "type": TicketValidatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipment",
                    "type": TicketingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipment",
                    "type": SeatingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipment",
                    "type": ShelterEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipment",
                    "type": TrolleyStandEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipment",
                    "type": WaitingRoomEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipment",
                    "type": CrossingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipment",
                    "type": QueueingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipment",
                    "type": EntranceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipment",
                    "type": RampEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipment",
                    "type": LiftEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipment",
                    "type": TravelatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipment",
                    "type": StaircaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipment",
                    "type": EscalatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLighting",
                    "type": PlaceLighting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurface",
                    "type": RoughSurface,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessEquipment",
                    "type": AccessEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSign",
                    "type": GeneralSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSign",
                    "type": HeadingSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSign",
                    "type": PlaceSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipment",
                    "type": SignEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleEquipment",
                    "type": WheelchairVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipment",
                    "type": AccessVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipment",
                    "type": VehicleChargingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipment",
                    "type": CycleStorageEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipment",
                    "type": PassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipment",
                    "type": HelpPointEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipment",
                    "type": PassengerSafetyEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePattern",
                    "type": ServicePattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPath",
                    "type": NavigationPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPattern",
                    "type": ServiceJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPattern",
                    "type": DeadRunJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern",
                    "type": JourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleRoute",
                    "type": FlexibleRoute,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Route",
                    "type": Route,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPattern",
                    "type": TimingPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Connection",
                    "type": Connection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnection",
                    "type": DefaultConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnection",
                    "type": SiteConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartment",
                    "type": OperatingDepartment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnit",
                    "type": OrganisationalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Department",
                    "type": Department,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPart",
                    "type": OrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortium",
                    "type": RetailConsortium,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisation",
                    "type": ServicedOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisation",
                    "type": GeneralOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgent",
                    "type": ManagementAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgent",
                    "type": TravelAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisation",
                    "type": OtherOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLink",
                    "type": ServiceLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLink",
                    "type": PathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLink",
                    "type": RouteLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLink",
                    "type": TimingLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireElement",
                    "type": WireElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadElement",
                    "type": RoadElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayElement",
                    "type": RailwayElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLink",
                    "type": ActivationLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPoint",
                    "type": BorderPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPoint",
                    "type": FareScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePoint",
                    "type": RoutePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPoint",
                    "type": TimingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireJunction",
                    "type": WireJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadJunction",
                    "type": RoadJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayJunction",
                    "type": RailwayJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPoint",
                    "type": TrafficControlPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Point",
                    "type": Point2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineShape",
                    "type": LineShape,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicProjection",
                    "type": TopographicProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjection",
                    "type": ZoneProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjection",
                    "type": ComplexFeatureProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjection",
                    "type": LinkSequenceProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjection",
                    "type": LinkProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjection",
                    "type": PointProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrame",
                    "type": ForwardRef("CompositeFrame"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrame",
                    "type": SalesTransactionFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrame",
                    "type": FareFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrame",
                    "type": DriverScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrame",
                    "type": VehicleScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrame",
                    "type": ServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrame",
                    "type": TimetableFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrame",
                    "type": SiteFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrame",
                    "type": InfrastructureFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrame",
                    "type": ForwardRef("GeneralFrame"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrame",
                    "type": ResourceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrame",
                    "type": ServiceCalendarFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriod",
                    "type": OperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDay",
                    "type": OperatingDay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendar",
                    "type": ServiceCalendar,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionAssignment",
                    "type": DistributionAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageSubstitution",
                    "type": SalesOfferPackageSubstitution,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchaseParameterAssignment",
                    "type": CustomerPurchaseParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecificParameterAssignment",
                    "type": SpecificParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityParameterAssignment",
                    "type": ValidityParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightParameterAssignment",
                    "type": AccessRightParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyAccounting",
                    "type": JourneyAccounting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandTypeAssignment",
                    "type": TimeDemandTypeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferRestriction",
                    "type": TransferRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceExclusion",
                    "type": ServiceExclusion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DisplayAssignment",
                    "type": DisplayAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintThroughput",
                    "type": CheckConstraintThroughput,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintDelay",
                    "type": CheckConstraintDelay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraint",
                    "type": CheckConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OvertakingPossibility",
                    "type": OvertakingPossibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingRestriction",
                    "type": MeetingRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedManoeuvre",
                    "type": RestrictedManoeuvre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeAtPoint",
                    "type": VehicleTypeAtPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationAssignment",
                    "type": ActivationAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesNoticeAssignment",
                    "type": SalesNoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignment",
                    "type": NoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeAssignment",
                    "type": DayTypeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebands",
                    "type": GroupOfTimebands,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Timeband",
                    "type": Timeband,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDayType",
                    "type": FareDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": OrganisationDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": DayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ResponsibilitySet",
                    "type": ResponsibilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValueSet",
                    "type": ValueSet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMachineReadability",
                    "type": TypeOfMachineReadability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcession",
                    "type": TypeOfConcession,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingMoment",
                    "type": ChargingMoment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameter",
                    "type": TypeOfUsageParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareTable",
                    "type": TypeOfFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPricingRule",
                    "type": TypeOfPricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnit",
                    "type": PriceUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingAlgorithmType",
                    "type": TimingAlgorithmType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfJourneyPartition",
                    "type": PurposeOfJourneyPartition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceFeature",
                    "type": TypeOfServiceFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassification",
                    "type": PointOfInterestClassification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Direction",
                    "type": Direction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfEquipmentProfile",
                    "type": PurposeOfEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityList",
                    "type": TypeOfSecurityList,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProductCategory",
                    "type": TypeOfProductCategory,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPaymentMethod",
                    "type": TypeOfPaymentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassOfUse",
                    "type": ClassOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Submode",
                    "type": Submode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OpenTransportMode",
                    "type": OpenTransportMode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCodespaceAssignment",
                    "type": TypeOfCodespaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfValidity",
                    "type": TypeOfValidity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfGrouping",
                    "type": PurposeOfGrouping,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Branding",
                    "type": Branding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DataSource",
                    "type": DataSource,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccount",
                    "type": TypeOfCustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntry",
                    "type": TypeOfFareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElement",
                    "type": TypeOfFareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariff",
                    "type": TypeOfTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactor",
                    "type": TypeOfFareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleService",
                    "type": TypeOfFlexibleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandType",
                    "type": TypeOfTimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipment",
                    "type": TypeOfPassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestion",
                    "type": TypeOfCongestion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPattern",
                    "type": TypeOfJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLine",
                    "type": TypeOfLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivation",
                    "type": TypeOfActivation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariant",
                    "type": TypeOfDeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNotice",
                    "type": TypeOfNotice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfService",
                    "type": TypeOfService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeature",
                    "type": TypeOfFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequence",
                    "type": TypeOfLinkSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlace",
                    "type": TypeOfPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransfer",
                    "type": TypeOfTransfer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperation",
                    "type": TypeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPart",
                    "type": TypeOfOrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisation",
                    "type": TypeOfOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZone",
                    "type": TypeOfZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLink",
                    "type": TypeOfLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPoint",
                    "type": TypeOfPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjection",
                    "type": TypeOfProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": TypeOfFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRole",
                    "type": TypeOfResponsibilityRole,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEntity",
                    "type": TypeOfEntity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfVersion",
                    "type": TypeOfVersion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeView",
                    "type": PassingTimeView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleAvailabilityCondition",
                    "type": SimpleAvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameter",
                    "type": ValidityRuleParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTrigger",
                    "type": ValidityTrigger,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityCondition",
                    "type": ValidityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Version",
                    "type": Version,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FramesRelStructure(ContainmentAggregationStructure):
    """
    Type for a collection of FRAMEs.
    """

    class Meta:
        name = "frames_RelStructure"

    choice: List[
        Union[
            SalesTransactionFrame,
            FareFrame,
            DriverScheduleFrame,
            VehicleScheduleFrame,
            ServiceFrame,
            TimetableFrame,
            SiteFrame,
            InfrastructureFrame,
            "GeneralFrame",
            ResourceFrame,
            ServiceCalendarFrame,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesTransactionFrame",
                    "type": SalesTransactionFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrame",
                    "type": FareFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrame",
                    "type": DriverScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrame",
                    "type": VehicleScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrame",
                    "type": ServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrame",
                    "type": TimetableFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrame",
                    "type": SiteFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrame",
                    "type": InfrastructureFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrame",
                    "type": ForwardRef("GeneralFrame"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrame",
                    "type": ResourceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrame",
                    "type": ServiceCalendarFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CompositeVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a COMPOSITE FRAME.

    :ivar frames: Content frames in COMPOSITE FRAME.
    """

    class Meta:
        name = "Composite_VersionFrameStructure"

    frames: Optional[FramesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class EntityEntityStructure(EntityStructure):
    """Type for a ENTITY.

    Will contain one or more versions of the appropriate ENTITY IN
    VERSION.

    :ivar versions: Versions of theENTITY.
    :ivar created: Date ENTITY was first created.
    :ivar changed: Date ENTITY or version was last changed.
    """

    class Meta:
        name = "Entity_EntityStructure"

    versions: EntitiesInVersionRelStructure = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class GeneralFrame(GeneralVersionFrameStructure):
    """A General purpose frame that can be used to exchange any NeTEx element.

    Does not impose any structure.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompositeFrame(CompositeVersionFrameStructure):
    """
    A container VERSION FRAME that groups a set of content VERSION FRAMsE to which
    the same VALIDITY CONDITIONs have been assigned.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntityEntity(EntityEntityStructure):
    """ENTITY.

    Will contain one or more ENTITY IN VERSIONs.
    """

    class Meta:
        name = "Entity_Entity"
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralFrameMembersRelStructure(ContainmentAggregationStructure):
    """
    A collection of one or more VERSION FRAME MEMBERS.
    """

    class Meta:
        name = "generalFrameMembers_RelStructure"

    choice: List[
        Union[
            GeneralFrameMember,
            TravelDocument,
            CustomerAccount,
            SalesTransaction,
            OfferedTravelSpecification,
            RequestedTravelSpecification,
            TravelSpecification1,
            TravelSpecification2,
            FareContractEntry,
            FareContract,
            Customer,
            ParkingTariff,
            GroupOfSalesOfferPackages,
            DistributionChannel,
            Tariff,
            CustomerPurchasePackage,
            SalesOfferPackage,
            FulfilmentMethod,
            CappingRule,
            EntitlementProduct,
            SupplementProduct,
            PreassignedFareProduct,
            AmountOfPriceUnitProduct,
            CappedDiscountRight,
            UsageDiscountRight,
            ThirdPartyProduct,
            SaleDiscountRight,
            ServiceAccessRight1,
            ServiceAccessRight2,
            TimeInterval,
            FareQuotaFactor,
            FareDemandFactor,
            QualityStructureFactor,
            ControllableElement,
            ValidableElement,
            SalesOfferPackageEntitlementRequired,
            SalesOfferPackageEntitlementGiven,
            MinimumStay,
            Interchanging,
            Suspending,
            UsageValidityPeriod,
            FrequencyOfUse,
            StepLimit,
            Routing,
            RoundTrip,
            LuggageAllowance,
            EntitlementRequired,
            EntitlementGiven,
            EligibilityChangePolicy,
            CompanionProfile,
            GroupTicket,
            CommercialProfile,
            UserProfile,
            Subscribing,
            PenaltyPolicy,
            ChargingPolicy,
            Cancelling,
            Reserving,
            PurchaseWindow,
            Transferability,
            Replacing,
            Refunding,
            Exchanging,
            Reselling,
            GeographicalInterval,
            SeriesConstraint,
            CustomerPurchasePackageElement,
            ParkingChargeBand,
            SalesOfferPackageElement,
            FareStructureElement,
            TimeStructureFactor,
            TimeUnit,
            DistanceMatrixElement,
            GeographicalStructureFactor,
            GeographicalUnit,
            FareUnit,
            FareInterval,
            FareStructureFactor,
            PricingService,
            LimitingRuleInContext,
            LimitingRule,
            DiscountingRule,
            PricingRule,
            MonthValidityOffset,
            Rounding,
            PricingParameterSet,
            ReliefOpportunity,
            CourseOfJourneys,
            VehicleServicePart,
            VehicleService,
            TrainBlockPart,
            CompoundBlock,
            BlockPart,
            TrainBlock,
            Block,
            DriverTripTime,
            DriverTrip,
            DutyPart,
            AccountableElement,
            Duty,
            TimeDemandProfile,
            VehicleTypeStopAssignment,
            TrainComponentLabelAssignment,
            TrainNumber,
            DatedSpecialService,
            NormalDatedVehicleJourney,
            DatedVehicleJourney,
            SpecialService,
            DeadRun,
            ServiceJourney,
            DatedServiceJourney,
            TemplateServiceJourney,
            TemplateVehicleJourney,
            VehicleJourney,
            FlexibleServiceProperties,
            JourneyPartCouple,
            CoupledJourney,
            JourneyPart,
            InterchangeRule,
            ServiceJourneyPatternInterchange,
            ServiceJourneyInterchange,
            DefaultInterchange,
            JourneyMeeting,
            PointOfInterestClassificationHierarchy,
            TimeDemandType,
            VehicleJourneyStopAssignment,
            FlexibleStopAssignment,
            NavigationPathAssignment,
            TrainStopAssignment,
            DynamicStopAssignment,
            PassengerStopAssignment,
            LogicalDisplay,
            Level,
            LineNetwork,
            RouteInstruction,
            AllowedLineDirection,
            DestinationDisplayVariant,
            DestinationDisplay,
            FlexibleLine,
            Line,
            OperationalContext,
            TrainComponent,
            TrainElement,
            CompoundTrain,
            Train,
            VehicleEquipmentProfile,
            VehicleModel,
            Vehicle,
            PassengerCarryingRequirementsView,
            FacilityRequirement,
            VehicleManoeuvringRequirement,
            PassengerCarryingRequirement,
            VehicleType,
            Whitelist,
            Blacklist,
            SchematicMap,
            DeliveryVariant,
            Notice,
            EquipmentPosition,
            AssistanceBookingService,
            CateringService,
            RetailService,
            MoneyService,
            HireService,
            CommunicationService,
            MeetingPointService,
            LostPropertyService,
            LeftLuggageService,
            ComplaintsService,
            CustomerService,
            LuggageService,
            AssistanceService,
            TicketingService,
            RetailDevice,
            TicketValidatorEquipment,
            TicketingEquipment,
            SeatingEquipment,
            ShelterEquipment,
            TrolleyStandEquipment,
            WaitingRoomEquipment,
            CrossingEquipment,
            QueueingEquipment,
            EntranceEquipment,
            RampEquipment,
            LiftEquipment,
            TravelatorEquipment,
            StaircaseEquipment,
            EscalatorEquipment,
            PlaceLighting,
            RoughSurface,
            AccessEquipment,
            GeneralSign,
            HeadingSign,
            PlaceSign,
            SignEquipment,
            WheelchairVehicleEquipment,
            AccessVehicleEquipment,
            VehicleChargingEquipment,
            CycleStorageEquipment,
            PassengerInformationEquipment,
            RubbishDisposalEquipment,
            HelpPointEquipment,
            PassengerSafetyEquipment,
            SanitaryEquipment,
            ServicePattern,
            NavigationPath,
            ServiceJourneyPattern,
            DeadRunJourneyPattern,
            JourneyPattern,
            FlexibleRoute,
            Route,
            TimingPattern,
            Connection,
            DefaultConnection,
            SiteConnection,
            Access,
            ControlCentre,
            OperatingDepartment,
            OrganisationalUnit,
            Department,
            OrganisationPart,
            RetailConsortium,
            Authority,
            Operator,
            ServicedOrganisation,
            GeneralOrganisation,
            ManagementAgent,
            TravelAgent,
            OtherOrganisation,
            ServiceLink,
            SitePathLink,
            PathLink,
            RouteLink,
            TimingLink,
            WireElement,
            RoadElement,
            RailwayElement,
            ActivationLink,
            BorderPoint,
            FareScheduledStopPoint,
            ScheduledStopPoint,
            PathJunction,
            RoutePoint,
            ParkingPoint,
            GaragePoint,
            ReliefPoint,
            TimingPoint,
            WireJunction,
            RoadJunction,
            RailwayJunction,
            TrafficControlPoint,
            BeaconPoint,
            ActivationPoint,
            Point2,
            LineShape,
            TopographicProjection,
            ZoneProjection,
            ComplexFeatureProjection,
            LinkSequenceProjection,
            LinkProjection,
            PointProjection,
            CompositeFrame,
            SalesTransactionFrame,
            FareFrame,
            DriverScheduleFrame,
            VehicleScheduleFrame,
            ServiceFrame,
            TimetableFrame,
            SiteFrame,
            InfrastructureFrame,
            GeneralFrame,
            ResourceFrame,
            ServiceCalendarFrame,
            UicOperatingPeriod,
            OperatingPeriod,
            OperatingDay,
            ServiceCalendar,
            DistributionAssignment,
            SalesOfferPackageSubstitution,
            CustomerPurchaseParameterAssignment,
            SpecificParameterAssignment,
            GenericParameterAssignmentInContext,
            GenericParameterAssignment,
            ValidityParameterAssignment,
            AccessRightParameterAssignment,
            JourneyAccounting,
            TimeDemandTypeAssignment,
            TransferRestriction,
            ServiceExclusion,
            DisplayAssignment,
            CheckConstraintThroughput,
            CheckConstraintDelay,
            CheckConstraint,
            OvertakingPossibility,
            MeetingRestriction,
            RestrictedManoeuvre,
            VehicleTypeAtPoint,
            ActivationAssignment,
            SalesNoticeAssignment,
            NoticeAssignment,
            DayTypeAssignment,
            GroupOfTimebands,
            Timeband,
            FareDayType,
            OrganisationDayType,
            DayType,
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
            ResponsibilitySet,
            ValueSet,
            TypeOfMachineReadability,
            TypeOfConcession,
            ChargingMoment,
            TypeOfUsageParameter,
            TypeOfFareTable,
            TypeOfPricingRule,
            PriceUnit,
            TimingAlgorithmType,
            PurposeOfJourneyPartition,
            TypeOfServiceFeature,
            PointOfInterestClassification,
            Direction,
            PurposeOfEquipmentProfile,
            TypeOfSecurityList,
            TypeOfProductCategory,
            TypeOfPaymentMethod,
            ClassOfUse,
            Submode,
            OpenTransportMode,
            TypeOfCodespaceAssignment,
            TypeOfValidity,
            PurposeOfGrouping,
            Branding,
            DataSource,
            TypeOfRetailDevice,
            CustomerAccountStatus,
            TypeOfCustomerAccount,
            TypeOfFareContractEntry,
            TypeOfFareContract,
            TypeOfTravelDocument,
            TypeOfSalesOfferPackage,
            TypeOfFareProduct,
            TypeOfFareStructureElement,
            TypeOfTariff,
            TypeOfAccessRightAssignment,
            TypeOfFareStructureFactor,
            TypeOfFlexibleService,
            TypeOfTimeDemandType,
            TypeOfPassengerInformationEquipment,
            TypeOfCongestion,
            TypeOfJourneyPattern,
            TypeOfLine,
            TypeOfActivation,
            TypeOfDeliveryVariant,
            TypeOfNotice,
            TypeOfFacility,
            TypeOfService,
            TypeOfEquipment,
            TypeOfFeature,
            TypeOfLinkSequence,
            TypeOfPlace,
            TypeOfTransfer,
            TypeOfOperation,
            TypeOfOrganisationPart,
            TypeOfOrganisation,
            TypeOfZone,
            TypeOfLink,
            TypeOfPoint,
            TypeOfProjection,
            TypeOfFrame,
            TypeOfResponsibilityRole,
            TypeOfEntity,
            TypeOfVersion,
            PassingTimeView,
            SimpleAvailabilityCondition,
            ValidDuring,
            AvailabilityCondition,
            ValidityRuleParameter,
            ValidityTrigger,
            ValidityCondition,
            Version,
            EntityEntity,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeneralFrameMember",
                    "type": GeneralFrameMember,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocument",
                    "type": TravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccount",
                    "type": CustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransaction",
                    "type": SalesTransaction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecification",
                    "type": RequestedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification",
                    "type": TravelSpecification1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification_",
                    "type": TravelSpecification2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntry_",
                    "type": FareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContract",
                    "type": FareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Customer",
                    "type": Customer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingTariff",
                    "type": ParkingTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackages",
                    "type": GroupOfSalesOfferPackages,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannel",
                    "type": DistributionChannel,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Tariff",
                    "type": Tariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackage",
                    "type": CustomerPurchasePackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackage",
                    "type": SalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethod",
                    "type": FulfilmentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRule",
                    "type": CappingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementProduct",
                    "type": EntitlementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProduct",
                    "type": SupplementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProduct",
                    "type": PreassignedFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProduct",
                    "type": AmountOfPriceUnitProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRight",
                    "type": CappedDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRight",
                    "type": UsageDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProduct",
                    "type": ThirdPartyProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRight",
                    "type": SaleDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRight",
                    "type": ServiceAccessRight1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRight_",
                    "type": ServiceAccessRight2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeInterval",
                    "type": TimeInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactor",
                    "type": QualityStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElement",
                    "type": ControllableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElement",
                    "type": ValidableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequired",
                    "type": SalesOfferPackageEntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGiven",
                    "type": SalesOfferPackageEntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStay",
                    "type": MinimumStay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Interchanging",
                    "type": Interchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Suspending",
                    "type": Suspending,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriod",
                    "type": UsageValidityPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUse",
                    "type": FrequencyOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimit",
                    "type": StepLimit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Routing",
                    "type": Routing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTrip",
                    "type": RoundTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowance",
                    "type": LuggageAllowance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequired",
                    "type": EntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGiven",
                    "type": EntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicy",
                    "type": EligibilityChangePolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicket",
                    "type": GroupTicket,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfile",
                    "type": CommercialProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfile",
                    "type": UserProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Subscribing",
                    "type": Subscribing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicy",
                    "type": PenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicy",
                    "type": ChargingPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Cancelling",
                    "type": Cancelling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reserving",
                    "type": Reserving,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindow",
                    "type": PurchaseWindow,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Transferability",
                    "type": Transferability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Replacing",
                    "type": Replacing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Refunding",
                    "type": Refunding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Exchanging",
                    "type": Exchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reselling",
                    "type": Reselling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalInterval",
                    "type": GeographicalInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraint",
                    "type": SeriesConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElement",
                    "type": CustomerPurchasePackageElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBand",
                    "type": ParkingChargeBand,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElement",
                    "type": SalesOfferPackageElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElement",
                    "type": FareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactor",
                    "type": TimeStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnit",
                    "type": TimeUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElement",
                    "type": DistanceMatrixElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactor",
                    "type": GeographicalStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnit",
                    "type": GeographicalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareUnit",
                    "type": FareUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareInterval",
                    "type": FareInterval,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureFactor",
                    "type": FareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingService",
                    "type": PricingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRuleInContext",
                    "type": LimitingRuleInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRule",
                    "type": LimitingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRule",
                    "type": DiscountingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRule",
                    "type": PricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonthValidityOffset",
                    "type": MonthValidityOffset,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Rounding",
                    "type": Rounding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingParameterSet",
                    "type": PricingParameterSet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefOpportunity",
                    "type": ReliefOpportunity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CourseOfJourneys",
                    "type": CourseOfJourneys,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePart",
                    "type": VehicleServicePart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleService",
                    "type": VehicleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockPart",
                    "type": TrainBlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundBlock",
                    "type": CompoundBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPart",
                    "type": BlockPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlock",
                    "type": TrainBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Block",
                    "type": Block,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripTime",
                    "type": DriverTripTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTrip",
                    "type": DriverTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyPart",
                    "type": DutyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccountableElement",
                    "type": AccountableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Duty",
                    "type": Duty,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandProfile",
                    "type": TimeDemandProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeStopAssignment",
                    "type": VehicleTypeStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentLabelAssignment",
                    "type": TrainComponentLabelAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumber",
                    "type": TrainNumber,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialService",
                    "type": DatedSpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourney",
                    "type": NormalDatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourney",
                    "type": DatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRun",
                    "type": DeadRun,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourney",
                    "type": ServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedServiceJourney",
                    "type": DatedServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourney",
                    "type": TemplateServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateVehicleJourney",
                    "type": TemplateVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourney",
                    "type": VehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServiceProperties",
                    "type": FlexibleServiceProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartCouple",
                    "type": JourneyPartCouple,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoupledJourney",
                    "type": CoupledJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPart",
                    "type": JourneyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRule",
                    "type": InterchangeRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternInterchange",
                    "type": ServiceJourneyPatternInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchange",
                    "type": ServiceJourneyInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultInterchange",
                    "type": DefaultInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyMeeting",
                    "type": JourneyMeeting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassificationHierarchy",
                    "type": PointOfInterestClassificationHierarchy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandType",
                    "type": TimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopAssignment",
                    "type": FlexibleStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathAssignment",
                    "type": NavigationPathAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignment",
                    "type": DynamicStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignment",
                    "type": PassengerStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogicalDisplay",
                    "type": LogicalDisplay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Level",
                    "type": Level,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineNetwork",
                    "type": LineNetwork,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteInstruction",
                    "type": RouteInstruction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirection",
                    "type": AllowedLineDirection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayVariant",
                    "type": DestinationDisplayVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplay",
                    "type": DestinationDisplay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLine",
                    "type": FlexibleLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Line",
                    "type": Line,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperationalContext",
                    "type": OperationalContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponent",
                    "type": TrainComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrain",
                    "type": CompoundTrain,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfile",
                    "type": VehicleEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleModel",
                    "type": VehicleModel,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Vehicle",
                    "type": Vehicle,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementsView",
                    "type": PassengerCarryingRequirementsView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilityRequirement",
                    "type": FacilityRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleManoeuvringRequirement",
                    "type": VehicleManoeuvringRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirement",
                    "type": PassengerCarryingRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleType",
                    "type": VehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Whitelist",
                    "type": Whitelist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Blacklist",
                    "type": Blacklist,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SchematicMap",
                    "type": SchematicMap,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeliveryVariant",
                    "type": DeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Notice",
                    "type": Notice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPosition",
                    "type": EquipmentPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingService",
                    "type": AssistanceBookingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringService",
                    "type": CateringService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailService",
                    "type": RetailService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyService",
                    "type": MoneyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireService",
                    "type": HireService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationService",
                    "type": CommunicationService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointService",
                    "type": MeetingPointService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyService",
                    "type": LostPropertyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageService",
                    "type": LeftLuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsService",
                    "type": ComplaintsService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerService",
                    "type": CustomerService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageService",
                    "type": LuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceService",
                    "type": AssistanceService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingService",
                    "type": TicketingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDevice",
                    "type": RetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipment",
                    "type": TicketValidatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipment",
                    "type": TicketingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipment",
                    "type": SeatingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipment",
                    "type": ShelterEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipment",
                    "type": TrolleyStandEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipment",
                    "type": WaitingRoomEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipment",
                    "type": CrossingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipment",
                    "type": QueueingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipment",
                    "type": EntranceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipment",
                    "type": RampEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipment",
                    "type": LiftEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipment",
                    "type": TravelatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipment",
                    "type": StaircaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipment",
                    "type": EscalatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLighting",
                    "type": PlaceLighting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurface",
                    "type": RoughSurface,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessEquipment",
                    "type": AccessEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSign",
                    "type": GeneralSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSign",
                    "type": HeadingSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSign",
                    "type": PlaceSign,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipment",
                    "type": SignEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleEquipment",
                    "type": WheelchairVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipment",
                    "type": AccessVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipment",
                    "type": VehicleChargingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipment",
                    "type": CycleStorageEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipment",
                    "type": PassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipment",
                    "type": HelpPointEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipment",
                    "type": PassengerSafetyEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePattern",
                    "type": ServicePattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPath",
                    "type": NavigationPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPattern",
                    "type": ServiceJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPattern",
                    "type": DeadRunJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern",
                    "type": JourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleRoute",
                    "type": FlexibleRoute,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Route",
                    "type": Route,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPattern",
                    "type": TimingPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Connection",
                    "type": Connection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnection",
                    "type": DefaultConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnection",
                    "type": SiteConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartment",
                    "type": OperatingDepartment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnit",
                    "type": OrganisationalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Department",
                    "type": Department,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPart",
                    "type": OrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortium",
                    "type": RetailConsortium,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisation",
                    "type": ServicedOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisation",
                    "type": GeneralOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgent",
                    "type": ManagementAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgent",
                    "type": TravelAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisation",
                    "type": OtherOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLink",
                    "type": ServiceLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLink",
                    "type": PathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLink",
                    "type": RouteLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLink",
                    "type": TimingLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireElement",
                    "type": WireElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadElement",
                    "type": RoadElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayElement",
                    "type": RailwayElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLink",
                    "type": ActivationLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPoint",
                    "type": BorderPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPoint",
                    "type": FareScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePoint",
                    "type": RoutePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPoint",
                    "type": TimingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireJunction",
                    "type": WireJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadJunction",
                    "type": RoadJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayJunction",
                    "type": RailwayJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPoint",
                    "type": TrafficControlPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Point",
                    "type": Point2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineShape",
                    "type": LineShape,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicProjection",
                    "type": TopographicProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjection",
                    "type": ZoneProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjection",
                    "type": ComplexFeatureProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjection",
                    "type": LinkSequenceProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjection",
                    "type": LinkProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjection",
                    "type": PointProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrame",
                    "type": CompositeFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrame",
                    "type": SalesTransactionFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrame",
                    "type": FareFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrame",
                    "type": DriverScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrame",
                    "type": VehicleScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrame",
                    "type": ServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrame",
                    "type": TimetableFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrame",
                    "type": SiteFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrame",
                    "type": InfrastructureFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrame",
                    "type": GeneralFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrame",
                    "type": ResourceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrame",
                    "type": ServiceCalendarFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriod",
                    "type": OperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDay",
                    "type": OperatingDay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendar",
                    "type": ServiceCalendar,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionAssignment",
                    "type": DistributionAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageSubstitution",
                    "type": SalesOfferPackageSubstitution,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchaseParameterAssignment",
                    "type": CustomerPurchaseParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecificParameterAssignment",
                    "type": SpecificParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityParameterAssignment",
                    "type": ValidityParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightParameterAssignment",
                    "type": AccessRightParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyAccounting",
                    "type": JourneyAccounting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandTypeAssignment",
                    "type": TimeDemandTypeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferRestriction",
                    "type": TransferRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceExclusion",
                    "type": ServiceExclusion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DisplayAssignment",
                    "type": DisplayAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintThroughput",
                    "type": CheckConstraintThroughput,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintDelay",
                    "type": CheckConstraintDelay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraint",
                    "type": CheckConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OvertakingPossibility",
                    "type": OvertakingPossibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingRestriction",
                    "type": MeetingRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedManoeuvre",
                    "type": RestrictedManoeuvre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeAtPoint",
                    "type": VehicleTypeAtPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationAssignment",
                    "type": ActivationAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesNoticeAssignment",
                    "type": SalesNoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignment",
                    "type": NoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeAssignment",
                    "type": DayTypeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebands",
                    "type": GroupOfTimebands,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Timeband",
                    "type": Timeband,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDayType",
                    "type": FareDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": OrganisationDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": DayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ResponsibilitySet",
                    "type": ResponsibilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValueSet",
                    "type": ValueSet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMachineReadability",
                    "type": TypeOfMachineReadability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcession",
                    "type": TypeOfConcession,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingMoment",
                    "type": ChargingMoment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameter",
                    "type": TypeOfUsageParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareTable",
                    "type": TypeOfFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPricingRule",
                    "type": TypeOfPricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnit",
                    "type": PriceUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingAlgorithmType",
                    "type": TimingAlgorithmType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfJourneyPartition",
                    "type": PurposeOfJourneyPartition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceFeature",
                    "type": TypeOfServiceFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassification",
                    "type": PointOfInterestClassification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Direction",
                    "type": Direction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfEquipmentProfile",
                    "type": PurposeOfEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityList",
                    "type": TypeOfSecurityList,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProductCategory",
                    "type": TypeOfProductCategory,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPaymentMethod",
                    "type": TypeOfPaymentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassOfUse",
                    "type": ClassOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Submode",
                    "type": Submode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OpenTransportMode",
                    "type": OpenTransportMode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCodespaceAssignment",
                    "type": TypeOfCodespaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfValidity",
                    "type": TypeOfValidity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfGrouping",
                    "type": PurposeOfGrouping,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Branding",
                    "type": Branding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DataSource",
                    "type": DataSource,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccount",
                    "type": TypeOfCustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntry",
                    "type": TypeOfFareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElement",
                    "type": TypeOfFareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariff",
                    "type": TypeOfTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactor",
                    "type": TypeOfFareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleService",
                    "type": TypeOfFlexibleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandType",
                    "type": TypeOfTimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipment",
                    "type": TypeOfPassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestion",
                    "type": TypeOfCongestion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPattern",
                    "type": TypeOfJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLine",
                    "type": TypeOfLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivation",
                    "type": TypeOfActivation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariant",
                    "type": TypeOfDeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNotice",
                    "type": TypeOfNotice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfService",
                    "type": TypeOfService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeature",
                    "type": TypeOfFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequence",
                    "type": TypeOfLinkSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlace",
                    "type": TypeOfPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransfer",
                    "type": TypeOfTransfer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperation",
                    "type": TypeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPart",
                    "type": TypeOfOrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisation",
                    "type": TypeOfOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZone",
                    "type": TypeOfZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLink",
                    "type": TypeOfLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPoint",
                    "type": TypeOfPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjection",
                    "type": TypeOfProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": TypeOfFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRole",
                    "type": TypeOfResponsibilityRole,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEntity",
                    "type": TypeOfEntity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfVersion",
                    "type": TypeOfVersion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeView",
                    "type": PassingTimeView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleAvailabilityCondition",
                    "type": SimpleAvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameter",
                    "type": ValidityRuleParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTrigger",
                    "type": ValidityTrigger,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityCondition",
                    "type": ValidityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Version",
                    "type": Version,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Entity_Entity",
                    "type": EntityEntity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
