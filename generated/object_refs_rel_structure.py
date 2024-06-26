from dataclasses import dataclass, field
from typing import List, Union

from generated.access_ref import AccessRef
from generated.access_right_in_product_ref import AccessRightInProductRef
from generated.access_space_ref import AccessSpaceRef
from generated.access_zone_ref import AccessZoneRef
from generated.accommodation_ref import AccommodationRef
from generated.accountable_element_ref import AccountableElementRef
from generated.activation_link_ref import ActivationLinkRef
from generated.activation_point_ref import ActivationPointRef
from generated.address_ref import AddressRef
from generated.addressable_place_ref import AddressablePlaceRef
from generated.administrative_zone_ref import AdministrativeZoneRef
from generated.all_authorities_ref import AllAuthoritiesRef
from generated.all_distribution_channels_ref import AllDistributionChannelsRef
from generated.all_operators_ref import AllOperatorsRef
from generated.all_organisations_ref import AllOrganisationsRef
from generated.all_transport_organisations_ref import (
    AllTransportOrganisationsRef,
)
from generated.allowed_line_direction_ref import AllowedLineDirectionRef
from generated.alternative_name_ref import AlternativeNameRef
from generated.alternative_text_ref import AlternativeTextRef
from generated.amount_of_price_unit_product_ref import (
    AmountOfPriceUnitProductRef,
)
from generated.authority_ref import AuthorityRef
from generated.availability_condition_ref import AvailabilityConditionRef
from generated.beacon_point_ref import BeaconPointRef
from generated.blacklist_ref import BlacklistRef
from generated.block_part_ref import BlockPartRef
from generated.block_ref import BlockRef
from generated.boarding_position_ref import BoardingPositionRef
from generated.border_point_ref import BorderPointRef
from generated.branding_ref import BrandingRef
from generated.cancelling_ref import CancellingRef
from generated.capped_discount_right_ref import CappedDiscountRightRef
from generated.capping_rule_price_ref import CappingRulePriceRef
from generated.capping_rule_ref import CappingRuleRef
from generated.cell_ref import CellRef
from generated.charging_moment_ref import ChargingMomentRef
from generated.charging_policy_ref import ChargingPolicyRef
from generated.class_of_use_ref import ClassOfUseRef
from generated.commercial_profile_eligibility_ref import (
    CommercialProfileEligibilityRef,
)
from generated.commercial_profile_ref import CommercialProfileRef
from generated.common_section_ref import CommonSectionRef
from generated.companion_profile_ref import CompanionProfileRef
from generated.complex_feature_projection_ref import (
    ComplexFeatureProjectionRef,
)
from generated.composite_frame_ref import CompositeFrameRef
from generated.compound_block_ref import CompoundBlockRef
from generated.compound_train_ref import CompoundTrainRef
from generated.connection_ref import ConnectionRef
from generated.control_centre_ref import ControlCentreRef
from generated.controllable_element_in_sequence_ref import (
    ControllableElementInSequenceRef,
)
from generated.controllable_element_price_ref import (
    ControllableElementPriceRef,
)
from generated.controllable_element_ref import ControllableElementRef
from generated.coupled_journey_ref import CoupledJourneyRef
from generated.course_of_journeys_ref import CourseOfJourneysRef
from generated.crew_base_ref import CrewBaseRef
from generated.customer_account_ref import CustomerAccountRef
from generated.customer_account_security_listing_ref import (
    CustomerAccountSecurityListingRef,
)
from generated.customer_account_status_ref import CustomerAccountStatusRef
from generated.customer_eligibility_ref import CustomerEligibilityRef
from generated.customer_purchase_package_element_ref import (
    CustomerPurchasePackageElementRef,
)
from generated.customer_purchase_package_price_ref import (
    CustomerPurchasePackagePriceRef,
)
from generated.customer_purchase_package_ref import CustomerPurchasePackageRef
from generated.customer_ref import CustomerRef
from generated.customer_security_listing_ref import CustomerSecurityListingRef
from generated.data_source_ref import DataSourceRef
from generated.dated_special_service_ref import DatedSpecialServiceRef
from generated.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from generated.day_type_ref import DayTypeRef
from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.dead_run_ref import DeadRunRef
from generated.default_connection_ref import DefaultConnectionRef
from generated.default_dead_run_run_time_ref import DefaultDeadRunRunTimeRef
from generated.default_interchange_ref import DefaultInterchangeRef
from generated.default_service_journey_time_ref import (
    DefaultServiceJourneyTimeRef,
)
from generated.delivery_variant_ref import DeliveryVariantRef
from generated.department_ref import DepartmentRef
from generated.destination_display_ref import DestinationDisplayRef
from generated.destination_display_variant_ref import (
    DestinationDisplayVariantRef,
)
from generated.direction_ref import DirectionRef
from generated.discounting_rule_ref import DiscountingRuleRef
from generated.distance_matrix_element_inverse_ref import (
    DistanceMatrixElementInverseRef,
)
from generated.distance_matrix_element_price_ref import (
    DistanceMatrixElementPriceRef,
)
from generated.distance_matrix_element_ref import DistanceMatrixElementRef
from generated.distribution_channel_ref import DistributionChannelRef
from generated.driver_ref import DriverRef
from generated.driver_schedule_frame_ref import DriverScheduleFrameRef
from generated.driver_trip_ref import DriverTripRef
from generated.driver_trip_time_ref import DriverTripTimeRef
from generated.duty_part_ref import DutyPartRef
from generated.duty_ref import DutyRef
from generated.eligibility_change_policy_ref import EligibilityChangePolicyRef
from generated.entitlement_given_ref import EntitlementGivenRef
from generated.entitlement_product_ref import EntitlementProductRef
from generated.entitlement_required_ref import EntitlementRequiredRef
from generated.entrance_ref import EntranceRef
from generated.equipment_place_ref import EquipmentPlaceRef
from generated.equipment_position_ref import EquipmentPositionRef
from generated.estimated_passing_time_ref import EstimatedPassingTimeRef
from generated.exchanging_ref import ExchangingRef
from generated.facility_ref import FacilityRef
from generated.facility_requirement_ref import FacilityRequirementRef
from generated.facility_set_ref import FacilitySetRef
from generated.fare_contract_entry_ref import FareContractEntryRef
from generated.fare_contract_ref import FareContractRef
from generated.fare_contract_security_listing_ref import (
    FareContractSecurityListingRef,
)
from generated.fare_day_type_ref import FareDayTypeRef
from generated.fare_demand_factor_ref import FareDemandFactorRef
from generated.fare_frame_ref import FareFrameRef
from generated.fare_price_ref import FarePriceRef
from generated.fare_product_price_ref import FareProductPriceRef
from generated.fare_product_ref import FareProductRef
from generated.fare_quota_factor_ref import FareQuotaFactorRef
from generated.fare_request_ref import FareRequestRef
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.fare_section_ref import FareSectionRef
from generated.fare_structure_element_in_sequence_ref import (
    FareStructureElementInSequenceRef,
)
from generated.fare_structure_element_price_ref import (
    FareStructureElementPriceRef,
)
from generated.fare_structure_element_ref import FareStructureElementRef
from generated.fare_table_column_ref import FareTableColumnRef
from generated.fare_table_ref import FareTableRef
from generated.fare_table_row_ref import FareTableRowRef
from generated.fare_zone_ref import FareZoneRef
from generated.flexible_area_ref import FlexibleAreaRef
from generated.flexible_line_ref import FlexibleLineRef
from generated.flexible_link_properties_ref import FlexibleLinkPropertiesRef
from generated.flexible_point_properties_ref import FlexiblePointPropertiesRef
from generated.flexible_quay_ref import FlexibleQuayRef
from generated.flexible_service_properties_ref import (
    FlexibleServicePropertiesRef,
)
from generated.flexible_stop_place_ref import FlexibleStopPlaceRef
from generated.frequency_of_use_ref import FrequencyOfUseRef
from generated.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from generated.fulfilment_method_ref import FulfilmentMethodRef
from generated.garage_point_ref import GaragePointRef
from generated.garage_ref import GarageRef
from generated.general_frame_ref import GeneralFrameRef
from generated.general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.general_section_ref import GeneralSectionRef
from generated.geographical_interval_price_ref import (
    GeographicalIntervalPriceRef,
)
from generated.geographical_interval_ref import GeographicalIntervalRef
from generated.geographical_structure_factor_ref import (
    GeographicalStructureFactorRef,
)
from generated.geographical_unit_price_ref import GeographicalUnitPriceRef
from generated.geographical_unit_ref import GeographicalUnitRef
from generated.group_of_customer_purchase_packages_ref import (
    GroupOfCustomerPurchasePackagesRef,
)
from generated.group_of_distance_matrix_elements_ref import (
    GroupOfDistanceMatrixElementsRef,
)
from generated.group_of_distribution_channels_ref import (
    GroupOfDistributionChannelsRef,
)
from generated.group_of_lines_ref import GroupOfLinesRef
from generated.group_of_operators_ref import GroupOfOperatorsRef
from generated.group_of_places_ref import GroupOfPlacesRef
from generated.group_of_sales_offer_packages_ref import (
    GroupOfSalesOfferPackagesRef,
)
from generated.group_of_services_ref import GroupOfServicesRef
from generated.group_of_stop_places_ref import GroupOfStopPlacesRef
from generated.group_of_timebands_ref import GroupOfTimebandsRef
from generated.group_of_timing_links_ref import GroupOfTimingLinksRef
from generated.group_ticket_ref import GroupTicketRef
from generated.hail_and_ride_area_ref import HailAndRideAreaRef
from generated.headway_journey_group_ref import HeadwayJourneyGroupRef
from generated.infrastructure_frame_ref import InfrastructureFrameRef
from generated.interchange_ref import InterchangeRef
from generated.interchange_rule_ref import InterchangeRuleRef
from generated.interchange_rule_timing_ref import InterchangeRuleTimingRef
from generated.interchanging_ref import InterchangingRef
from generated.journey_frequency_group_ref import JourneyFrequencyGroupRef
from generated.journey_meeting_ref import JourneyMeetingRef
from generated.journey_part_couple_ref import JourneyPartCoupleRef
from generated.journey_part_ref import JourneyPartRef
from generated.journey_pattern_headway_ref import JourneyPatternHeadwayRef
from generated.journey_pattern_layover_ref import JourneyPatternLayoverRef
from generated.journey_pattern_ref import JourneyPatternRef
from generated.journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from generated.journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from generated.journey_timing_ref import JourneyTimingRef
from generated.layer_ref import LayerRef
from generated.level_ref import LevelRef
from generated.limiting_rule_ref import LimitingRuleRef
from generated.line_link_ref import LineLinkRef
from generated.line_network_ref import LineNetworkRef
from generated.line_ref import LineRef
from generated.line_section_ref import LineSectionRef
from generated.link_projection_ref import LinkProjectionRef
from generated.link_sequence_projection_ref import LinkSequenceProjectionRef
from generated.link_sequence_ref import LinkSequenceRef
from generated.log_entry_ref import LogEntryRef
from generated.log_ref import LogRef
from generated.logical_display_ref import LogicalDisplayRef
from generated.luggage_allowance_ref import LuggageAllowanceRef
from generated.management_agent_ref import ManagementAgentRef
from generated.minimum_stay_ref import MinimumStayRef
from generated.mode_ref import ModeRef
from generated.month_validity_offset_ref import MonthValidityOffsetRef
from generated.navigation_path_ref import NavigationPathRef
from generated.network_ref import NetworkRef
from generated.notice_ref import NoticeRef
from generated.observed_passing_time_ref import ObservedPassingTimeRef
from generated.offered_travel_specification_ref import (
    OfferedTravelSpecificationRef,
)
from generated.onboard_stay_ref import OnboardStayRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.open_transport_mode_ref import OpenTransportModeRef
from generated.operating_day_ref import OperatingDayRef
from generated.operating_department_ref import OperatingDepartmentRef
from generated.operating_period_ref import OperatingPeriodRef
from generated.operational_context_ref import OperationalContextRef
from generated.operator_ref import OperatorRef
from generated.organisation_part_ref import OrganisationPartRef
from generated.organisation_ref import OrganisationRef
from generated.organisational_unit_ref import OrganisationalUnitRef
from generated.other_organisation_ref import OtherOrganisationRef
from generated.parent_common_section_ref import ParentCommonSectionRef
from generated.parent_section_ref import ParentSectionRef
from generated.parking_area_ref import ParkingAreaRef
from generated.parking_bay_ref import ParkingBayRef
from generated.parking_capacity_ref import ParkingCapacityRef
from generated.parking_charge_band_ref import ParkingChargeBandRef
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)
from generated.parking_entrance_ref import ParkingEntranceRef
from generated.parking_passenger_entrance_ref import (
    ParkingPassengerEntranceRef,
)
from generated.parking_point_ref import ParkingPointRef
from generated.parking_price_ref import ParkingPriceRef
from generated.parking_properties_ref import ParkingPropertiesRef
from generated.parking_ref import ParkingRef
from generated.parking_tariff_ref import ParkingTariffRef
from generated.passenger_capacity_ref import PassengerCapacityRef
from generated.passenger_carrying_requirement_ref import (
    PassengerCarryingRequirementRef,
)
from generated.passenger_seat_ref import PassengerSeatRef
from generated.passing_time_ref import PassingTimeRef
from generated.path_junction_ref import PathJunctionRef
from generated.path_link_ref import PathLinkRef
from generated.penalty_policy_ref import PenaltyPolicyRef
from generated.place_ref import PlaceRef
from generated.point_of_interest_classification_ref import (
    PointOfInterestClassificationRef,
)
from generated.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from generated.point_of_interest_hierarchy_ref import (
    PointOfInterestHierarchyRef,
)
from generated.point_of_interest_ref import PointOfInterestRef
from generated.point_of_interest_space_ref import PointOfInterestSpaceRef
from generated.point_of_interest_vehicle_entrance_ref import (
    PointOfInterestVehicleEntranceRef,
)
from generated.point_projection_ref import PointProjectionRef
from generated.point_ref import PointRef
from generated.postal_address_ref import PostalAddressRef
from generated.preassigned_fare_product_ref import PreassignedFareProductRef
from generated.price_group_ref import PriceGroupRef
from generated.price_unit_ref import PriceUnitRef
from generated.priceable_object_ref import PriceableObjectRef
from generated.pricing_parameter_set_ref import PricingParameterSetRef
from generated.pricing_rule_ref import PricingRuleRef
from generated.pricing_service_ref import PricingServiceRef
from generated.profile_parameter_ref import ProfileParameterRef
from generated.purchase_window_ref import PurchaseWindowRef
from generated.purpose_of_equipment_profile_ref import (
    PurposeOfEquipmentProfileRef,
)
from generated.purpose_of_grouping_ref import PurposeOfGroupingRef
from generated.purpose_of_journey_partition_ref import (
    PurposeOfJourneyPartitionRef,
)
from generated.quality_structure_factor_price_ref import (
    QualityStructureFactorPriceRef,
)
from generated.quality_structure_factor_ref import QualityStructureFactorRef
from generated.quay_ref import QuayRef
from generated.railway_link_ref import RailwayLinkRef
from generated.railway_point_ref import RailwayPointRef
from generated.refunding_ref import RefundingRef
from generated.relief_opportunity_ref import ReliefOpportunityRef
from generated.relief_point_ref import ReliefPointRef
from generated.repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from generated.replacing_ref import ReplacingRef
from generated.requested_travel_specification_ref import (
    RequestedTravelSpecificationRef,
)
from generated.reselling_ref import ResellingRef
from generated.reserving_ref import ReservingRef
from generated.residential_qualification_eligibility_ref import (
    ResidentialQualificationEligibilityRef,
)
from generated.residential_qualification_ref import ResidentialQualificationRef
from generated.resource_frame_ref import ResourceFrameRef
from generated.responsibility_role_ref import ResponsibilityRoleRef
from generated.responsibility_set_ref import ResponsibilitySetRef
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.retail_device_security_listing_ref import (
    RetailDeviceSecurityListingRef,
)
from generated.rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from generated.road_address_ref import RoadAddressRef
from generated.road_link_ref import RoadLinkRef
from generated.road_point_ref import RoadPointRef
from generated.round_trip_ref import RoundTripRef
from generated.rounding_ref import RoundingRef
from generated.rounding_step_ref import RoundingStepRef
from generated.route_instruction_ref import RouteInstructionRef
from generated.route_link_ref import RouteLinkRef
from generated.route_point_ref import RoutePointRef
from generated.route_ref import RouteRef
from generated.routing_constraint_zone_ref import RoutingConstraintZoneRef
from generated.routing_ref import RoutingRef
from generated.sale_discount_right_ref import SaleDiscountRightRef
from generated.sales_offer_package_element_ref import (
    SalesOfferPackageElementRef,
)
from generated.sales_offer_package_entitlement_given_ref import (
    SalesOfferPackageEntitlementGivenRef,
)
from generated.sales_offer_package_entitlement_required_ref import (
    SalesOfferPackageEntitlementRequiredRef,
)
from generated.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from generated.sales_offer_package_ref import SalesOfferPackageRef
from generated.sales_transaction_frame_ref import SalesTransactionFrameRef
from generated.sales_transaction_ref import SalesTransactionRef
from generated.schedule_request_ref import ScheduleRequestRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.schematic_map_member_ref import SchematicMapMemberRef
from generated.schematic_map_ref import SchematicMapRef
from generated.section_ref import SectionRef
from generated.series_constraint_price_ref import SeriesConstraintPriceRef
from generated.series_constraint_ref import SeriesConstraintRef
from generated.service_access_right_ref import ServiceAccessRightRef
from generated.service_calendar_frame_ref import ServiceCalendarFrameRef
from generated.service_calendar_ref import ServiceCalendarRef
from generated.service_facility_set_ref import ServiceFacilitySetRef
from generated.service_frame_ref import ServiceFrameRef
from generated.service_journey_interchange_ref import (
    ServiceJourneyInterchangeRef,
)
from generated.service_journey_pattern_interchange_ref import (
    ServiceJourneyPatternInterchangeRef,
)
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_journey_ref import ServiceJourneyRef
from generated.service_link_ref import ServiceLinkRef
from generated.service_pattern_ref import ServicePatternRef
from generated.service_site_ref import ServiceSiteRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.single_trip_fare_request_ref import SingleTripFareRequestRef
from generated.site_component_ref import SiteComponentRef
from generated.site_connection_ref import SiteConnectionRef
from generated.site_element_ref import SiteElementRef
from generated.site_facility_set_ref import SiteFacilitySetRef
from generated.site_frame_ref import SiteFrameRef
from generated.site_ref import SiteRef
from generated.special_service_ref import SpecialServiceRef
from generated.standard_fare_table_ref import StandardFareTableRef
from generated.start_time_at_stop_point_ref import StartTimeAtStopPointRef
from generated.step_limit_ref import StepLimitRef
from generated.stop_area_ref import StopAreaRef
from generated.stop_event_request_ref import StopEventRequestRef
from generated.stop_finder_request_ref import StopFinderRequestRef
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.stop_place_ref import StopPlaceRef
from generated.stop_place_space_ref import StopPlaceSpaceRef
from generated.stop_place_vehicle_entrance_ref import (
    StopPlaceVehicleEntranceRef,
)
from generated.submode_ref import SubmodeRef
from generated.subscribing_ref import SubscribingRef
from generated.supplement_product_ref import SupplementProductRef
from generated.supply_contract_ref import SupplyContractRef
from generated.suspending_ref import SuspendingRef
from generated.target_passing_time_ref import TargetPassingTimeRef
from generated.tariff_object_ref import TariffObjectRef
from generated.tariff_ref import TariffRef
from generated.tariff_zone_ref import TariffZoneRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.third_party_product_ref import ThirdPartyProductRef
from generated.time_demand_profile_ref import TimeDemandProfileRef
from generated.time_demand_type_ref import TimeDemandTypeRef
from generated.time_interval_price_ref import TimeIntervalPriceRef
from generated.time_interval_ref import TimeIntervalRef
from generated.time_structure_factor_ref import TimeStructureFactorRef
from generated.time_unit_price_ref import TimeUnitPriceRef
from generated.time_unit_ref import TimeUnitRef
from generated.timeband_ref import TimebandRef
from generated.timetable_frame_ref import TimetableFrameRef
from generated.timetabled_passing_time_ref import TimetabledPassingTimeRef
from generated.timing_algorithm_type_ref import TimingAlgorithmTypeRef
from generated.timing_link_ref import TimingLinkRef
from generated.timing_pattern_ref import TimingPatternRef
from generated.timing_point_ref import TimingPointRef
from generated.topographic_place_ref import TopographicPlaceRef
from generated.topographic_projection_ref import TopographicProjectionRef
from generated.traffic_control_point_ref import TrafficControlPointRef
from generated.train_block_part_ref import TrainBlockPartRef
from generated.train_block_ref import TrainBlockRef
from generated.train_component_ref import TrainComponentRef
from generated.train_element_ref import TrainElementRef
from generated.train_in_compound_train_ref import TrainInCompoundTrainRef
from generated.train_number_ref import TrainNumberRef
from generated.train_ref import TrainRef
from generated.transferability_ref import TransferabilityRef
from generated.transport_administrative_zone_ref import (
    TransportAdministrativeZoneRef,
)
from generated.travel_agent_ref import TravelAgentRef
from generated.travel_document_ref import TravelDocumentRef
from generated.travel_document_security_listing_ref import (
    TravelDocumentSecurityListingRef,
)
from generated.travel_specification_ref import TravelSpecificationRef
from generated.trip_plan_request_ref import TripPlanRequestRef
from generated.turnaround_time_limit_time_ref import TurnaroundTimeLimitTimeRef
from generated.type_of_access_right_assignment_ref import (
    TypeOfAccessRightAssignmentRef,
)
from generated.type_of_activation_ref import TypeOfActivationRef
from generated.type_of_codespace_assignment_ref import (
    TypeOfCodespaceAssignmentRef,
)
from generated.type_of_concession_ref import TypeOfConcessionRef
from generated.type_of_congestion_ref import TypeOfCongestionRef
from generated.type_of_customer_account_ref import TypeOfCustomerAccountRef
from generated.type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from generated.type_of_equipment_ref import TypeOfEquipmentRef
from generated.type_of_facility_ref import TypeOfFacilityRef
from generated.type_of_fare_contract_entry_ref import (
    TypeOfFareContractEntryRef,
)
from generated.type_of_fare_contract_ref import TypeOfFareContractRef
from generated.type_of_fare_product_ref import TypeOfFareProductRef
from generated.type_of_fare_structure_element_ref import (
    TypeOfFareStructureElementRef,
)
from generated.type_of_fare_structure_factor_ref import (
    TypeOfFareStructureFactorRef,
)
from generated.type_of_fare_table_ref import TypeOfFareTableRef
from generated.type_of_feature_ref import TypeOfFeatureRef
from generated.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from generated.type_of_frame_ref import TypeOfFrameRef
from generated.type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from generated.type_of_line_ref import TypeOfLineRef
from generated.type_of_link_ref import TypeOfLinkRef
from generated.type_of_link_sequence_ref import TypeOfLinkSequenceRef
from generated.type_of_machine_readability_ref import (
    TypeOfMachineReadabilityRef,
)
from generated.type_of_notice_ref import TypeOfNoticeRef
from generated.type_of_operation_ref import TypeOfOperationRef
from generated.type_of_organisation_part_ref import TypeOfOrganisationPartRef
from generated.type_of_organisation_ref import TypeOfOrganisationRef
from generated.type_of_passenger_information_equipment_ref import (
    TypeOfPassengerInformationEquipmentRef,
)
from generated.type_of_payment_method_ref import TypeOfPaymentMethodRef
from generated.type_of_place_ref import TypeOfPlaceRef
from generated.type_of_point_ref import TypeOfPointRef
from generated.type_of_pricing_rule_ref import TypeOfPricingRuleRef
from generated.type_of_product_category_ref import TypeOfProductCategoryRef
from generated.type_of_projection_ref import TypeOfProjectionRef
from generated.type_of_responsibility_role_ref import (
    TypeOfResponsibilityRoleRef,
)
from generated.type_of_retail_device_ref import TypeOfRetailDeviceRef
from generated.type_of_sales_offer_package_ref import (
    TypeOfSalesOfferPackageRef,
)
from generated.type_of_security_list_ref import TypeOfSecurityListRef
from generated.type_of_service_feature_ref import TypeOfServiceFeatureRef
from generated.type_of_service_ref import TypeOfServiceRef
from generated.type_of_tariff_ref import TypeOfTariffRef
from generated.type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from generated.type_of_transfer_ref import TypeOfTransferRef
from generated.type_of_travel_document_ref import TypeOfTravelDocumentRef
from generated.type_of_usage_parameter_ref import TypeOfUsageParameterRef
from generated.type_of_validity_ref import TypeOfValidityRef
from generated.type_of_zone_ref import TypeOfZoneRef
from generated.usage_discount_right_ref import UsageDiscountRightRef
from generated.usage_parameter_price_ref import UsageParameterPriceRef
from generated.usage_validity_period_ref import UsageValidityPeriodRef
from generated.user_profile_eligibility_ref import UserProfileEligibilityRef
from generated.user_profile_ref import UserProfileRef
from generated.validable_element_price_ref import ValidableElementPriceRef
from generated.validable_element_ref import ValidableElementRef
from generated.validity_condition_ref import ValidityConditionRef
from generated.validity_rule_parameter_ref import ValidityRuleParameterRef
from generated.validity_trigger_ref import ValidityTriggerRef
from generated.vehicle_entrance_ref import VehicleEntranceRef
from generated.vehicle_equipment_profile_ref import VehicleEquipmentProfileRef
from generated.vehicle_journey_ref import VehicleJourneyRef
from generated.vehicle_manoeuvring_requirement_ref import (
    VehicleManoeuvringRequirementRef,
)
from generated.vehicle_model_ref import VehicleModelRef
from generated.vehicle_position_alignment_ref import (
    VehiclePositionAlignmentRef,
)
from generated.vehicle_quay_alignment_ref import VehicleQuayAlignmentRef
from generated.vehicle_ref import VehicleRef
from generated.vehicle_requirement_ref import VehicleRequirementRef
from generated.vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from generated.vehicle_service_part_ref import VehicleServicePartRef
from generated.vehicle_service_ref import VehicleServiceRef
from generated.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from generated.vehicle_stopping_position_ref import VehicleStoppingPositionRef
from generated.vehicle_type_preference_ref import VehicleTypePreferenceRef
from generated.vehicle_type_ref import VehicleTypeRef
from generated.version_of_object_ref import VersionOfObjectRef
from generated.version_ref import VersionRef
from generated.whitelist_ref import WhitelistRef
from generated.wire_link_ref import WireLinkRef
from generated.wire_point_ref import WirePointRef
from generated.zone_projection_ref import ZoneProjectionRef
from generated.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObjectRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to an  NeTEx Object.
    """

    class Meta:
        name = "objectRefs_RelStructure"

    choice: List[
        Union[
            TravelDocumentRef,
            RepeatedTripFareRequestRef,
            SingleTripFareRequestRef,
            FareRequestRef,
            StopFinderRequestRef,
            StopEventRequestRef,
            ScheduleRequestRef,
            TripPlanRequestRef,
            ResidentialQualificationEligibilityRef,
            CommercialProfileEligibilityRef,
            UserProfileEligibilityRef,
            CustomerEligibilityRef,
            CustomerAccountRef,
            FareContractRef,
            CustomerRef,
            StartTimeAtStopPointRef,
            ResidentialQualificationRef,
            TypeOfConcessionRef,
            TypeOfUsageParameterRef,
            TariffObjectRef,
            ParkingTariffRef,
            TariffRef,
            TypeOfFareTableRef,
            FareTableRowRef,
            FareTableColumnRef,
            TimeUnitRef,
            GeographicalUnitRef,
            ControllableElementInSequenceRef,
            FareStructureElementInSequenceRef,
            AccessRightInProductRef,
            CellRef,
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            SeriesConstraintPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
            CustomerPurchasePackageElementRef,
            CustomerPurchasePackageRef,
            ControllableElementRef,
            ValidableElementRef,
            SalesOfferPackageEntitlementGivenRef,
            SalesOfferPackageEntitlementRequiredRef,
            MinimumStayRef,
            InterchangingRef,
            FrequencyOfUseRef,
            SuspendingRef,
            UsageValidityPeriodRef,
            StepLimitRef,
            RoutingRef,
            RoundTripRef,
            LuggageAllowanceRef,
            EntitlementGivenRef,
            EntitlementRequiredRef,
            EligibilityChangePolicyRef,
            GroupTicketRef,
            CommercialProfileRef,
            CompanionProfileRef,
            UserProfileRef,
            ProfileParameterRef,
            SubscribingRef,
            PenaltyPolicyRef,
            ChargingPolicyRef,
            TransferabilityRef,
            ReplacingRef,
            RefundingRef,
            ExchangingRef,
            ResellingRef,
            CancellingRef,
            ReservingRef,
            PurchaseWindowRef,
            SalesOfferPackageElementRef,
            SalesOfferPackageRef,
            DistanceMatrixElementInverseRef,
            DistanceMatrixElementRef,
            FareStructureElementRef,
            FulfilmentMethodRef,
            SeriesConstraintRef,
            CappingRuleRef,
            EntitlementProductRef,
            SupplementProductRef,
            PreassignedFareProductRef,
            AmountOfPriceUnitProductRef,
            UsageDiscountRightRef,
            ThirdPartyProductRef,
            CappedDiscountRightRef,
            SaleDiscountRightRef,
            FareProductRef,
            ServiceAccessRightRef,
            TimeIntervalRef,
            GeographicalIntervalRef,
            ParkingChargeBandRef,
            TimeStructureFactorRef,
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            GeographicalStructureFactorRef,
            PriceableObjectRef,
            MonthValidityOffsetRef,
            LimitingRuleRef,
            DiscountingRuleRef,
            PricingRuleRef,
            PricingServiceRef,
            RoundingStepRef,
            RoundingRef,
            PricingParameterSetRef,
            SupplyContractRef,
            FlexibleServicePropertiesRef,
            DriverTripTimeRef,
            DriverTripRef,
            DutyPartRef,
            AccountableElementRef,
            DutyRef,
            ReliefOpportunityRef,
            CourseOfJourneysRef,
            DriverRef,
            VehicleServicePartRef,
            VehicleServiceRef,
            CompoundBlockRef,
            TrainBlockPartRef,
            BlockPartRef,
            TrainBlockRef,
            BlockRef,
            JourneyPartCoupleRef,
            CoupledJourneyRef,
            JourneyPartRef,
            TimetabledPassingTimeRef,
            EstimatedPassingTimeRef,
            ObservedPassingTimeRef,
            TargetPassingTimeRef,
            PassingTimeRef,
            InterchangeRuleTimingRef,
            InterchangeRuleRef,
            ServiceJourneyPatternInterchangeRef,
            ServiceJourneyInterchangeRef,
            DefaultInterchangeRef,
            InterchangeRef,
            JourneyMeetingRef,
            TrainNumberRef,
            RoutingConstraintZoneRef,
            VehiclePositionAlignmentRef,
            VehicleQuayAlignmentRef,
            LogicalDisplayRef,
            ParkingAreaRef,
            ParkingPropertiesRef,
            ParkingCapacityRef,
            LineNetworkRef,
            RouteInstructionRef,
            LevelRef,
            FlexiblePointPropertiesRef,
            FlexibleLinkPropertiesRef,
            TimeDemandProfileRef,
            TimeDemandTypeRef,
            VehicleTypePreferenceRef,
            JourneyPatternHeadwayRef,
            JourneyPatternLayoverRef,
            JourneyPatternRunTimeRef,
            JourneyPatternWaitTimeRef,
            DefaultServiceJourneyTimeRef,
            DefaultDeadRunRunTimeRef,
            TurnaroundTimeLimitTimeRef,
            JourneyTimingRef,
            CrewBaseRef,
            PassengerSeatRef,
            OperatingDepartmentRef,
            OperationalContextRef,
            TrainComponentRef,
            TrainElementRef,
            TrainInCompoundTrainRef,
            TravelDocumentSecurityListingRef,
            RetailDeviceSecurityListingRef,
            CustomerAccountSecurityListingRef,
            FareContractSecurityListingRef,
            CustomerSecurityListingRef,
            WhitelistRef,
            BlacklistRef,
            SchematicMapMemberRef,
            SchematicMapRef,
            DeliveryVariantRef,
            NoticeRef,
            VehicleEquipmentProfileRef,
            VehicleModelRef,
            VehicleRef,
            PassengerCapacityRef,
            FacilityRequirementRef,
            VehicleManoeuvringRequirementRef,
            PassengerCarryingRequirementRef,
            VehicleRequirementRef,
            CompoundTrainRef,
            TrainRef,
            VehicleTypeRef,
            OnboardStayRef,
            AccommodationRef,
            ServiceFacilitySetRef,
            SiteFacilitySetRef,
            FacilitySetRef,
            FacilityRef,
            ModeRef,
            SubmodeRef,
            OpenTransportModeRef,
            TopographicProjectionRef,
            ComplexFeatureProjectionRef,
            LinkSequenceProjectionRef,
            ZoneProjectionRef,
            LinkProjectionRef,
            PointProjectionRef,
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
            NavigationPathRef,
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
            TimingPatternRef,
            RouteRef,
            LinkSequenceRef,
            SalesTransactionRef,
            OfferedTravelSpecificationRef,
            RequestedTravelSpecificationRef,
            TravelSpecificationRef,
            FareContractEntryRef,
            LogEntryRef,
            AlternativeNameRef,
            TimebandRef,
            FareDayTypeRef,
            DayTypeRef,
            DefaultConnectionRef,
            SiteConnectionRef,
            ConnectionRef,
            AccessRef,
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
            ServiceLinkRef,
            LineLinkRef,
            PathLinkRef,
            TimingLinkRef,
            RouteLinkRef,
            WireLinkRef,
            RoadLinkRef,
            RailwayLinkRef,
            ActivationLinkRef,
            BorderPointRef,
            FareScheduledStopPointRef,
            ScheduledStopPointRef,
            GaragePointRef,
            ParkingPointRef,
            ReliefPointRef,
            TimingPointRef,
            RoutePointRef,
            WirePointRef,
            RoadPointRef,
            RailwayPointRef,
            TrafficControlPointRef,
            BeaconPointRef,
            ActivationPointRef,
            PointRef,
            OperatingPeriodRef,
            OperatingDayRef,
            ServiceCalendarRef,
            AlternativeTextRef,
            AvailabilityConditionRef,
            ValidityRuleParameterRef,
            ValidityTriggerRef,
            ValidityConditionRef,
            ResponsibilityRoleRef,
            ControlCentreRef,
            OrganisationalUnitRef,
            DepartmentRef,
            OrganisationPartRef,
            AllAuthoritiesRef,
            AllOperatorsRef,
            AllTransportOrganisationsRef,
            AllOrganisationsRef,
            RetailConsortiumRef,
            AuthorityRef,
            OperatorRef,
            GeneralOrganisationRef,
            ManagementAgentRef,
            ServicedOrganisationRef,
            TravelAgentRef,
            OtherOrganisationRef,
            OrganisationRef,
            ResponsibilitySetRef,
            DestinationDisplayVariantRef,
            DestinationDisplayRef,
            AllowedLineDirectionRef,
            FlexibleLineRef,
            LineRef,
            GroupOfCustomerPurchasePackagesRef,
            GroupOfSalesOfferPackagesRef,
            GroupOfDistanceMatrixElementsRef,
            GroupOfDistributionChannelsRef,
            StandardFareTableRef,
            FareTableRef,
            PriceGroupRef,
            RhythmicalJourneyGroupRef,
            HeadwayJourneyGroupRef,
            JourneyFrequencyGroupRef,
            GroupOfServicesRef,
            GroupOfStopPlacesRef,
            PointOfInterestHierarchyRef,
            GroupOfTimingLinksRef,
            GroupOfOperatorsRef,
            GroupOfPlacesRef,
            ParentSectionRef,
            ParentCommonSectionRef,
            CommonSectionRef,
            LineSectionRef,
            FareSectionRef,
            GeneralSectionRef,
            SectionRef,
            LogRef,
            GroupOfTimebandsRef,
            PlaceRef,
            StopAreaRef,
            AccessZoneRef,
            TransportAdministrativeZoneRef,
            AdministrativeZoneRef,
            FareZoneRef,
            TariffZoneRef,
            ZoneRef,
            LayerRef,
            NetworkRef,
            GroupOfLinesRef,
            GeneralGroupOfEntitiesRef,
            SalesTransactionFrameRef,
            FareFrameRef,
            ServiceFrameRef,
            DriverScheduleFrameRef,
            VehicleScheduleFrameRef,
            TimetableFrameRef,
            SiteFrameRef,
            InfrastructureFrameRef,
            GeneralFrameRef,
            ResourceFrameRef,
            ServiceCalendarFrameRef,
            CompositeFrameRef,
            DistributionChannelRef,
            ChargingMomentRef,
            PriceUnitRef,
            PurposeOfJourneyPartitionRef,
            TimingAlgorithmTypeRef,
            PointOfInterestClassificationRef,
            DirectionRef,
            TypeOfActivationRef,
            PurposeOfEquipmentProfileRef,
            TypeOfProductCategoryRef,
            TypeOfPaymentMethodRef,
            ClassOfUseRef,
            TypeOfOperationRef,
            TypeOfCodespaceAssignmentRef,
            BrandingRef,
            TypeOfResponsibilityRoleRef,
            PurposeOfGroupingRef,
            TypeOfRetailDeviceRef,
            CustomerAccountStatusRef,
            TypeOfCustomerAccountRef,
            TypeOfFareContractEntryRef,
            TypeOfFareContractRef,
            TypeOfAccessRightAssignmentRef,
            TypeOfSalesOfferPackageRef,
            TypeOfFareStructureElementRef,
            TypeOfTariffRef,
            AllDistributionChannelsRef,
            TypeOfMachineReadabilityRef,
            TypeOfTravelDocumentRef,
            TypeOfFareProductRef,
            TypeOfFareStructureFactorRef,
            TypeOfPricingRuleRef,
            TypeOfFlexibleServiceRef,
            TypeOfPassengerInformationEquipmentRef,
            TypeOfServiceFeatureRef,
            TypeOfCongestionRef,
            TypeOfTimeDemandTypeRef,
            TypeOfJourneyPatternRef,
            TypeOfSecurityListRef,
            TypeOfDeliveryVariantRef,
            TypeOfNoticeRef,
            TypeOfServiceRef,
            TypeOfFacilityRef,
            TypeOfEquipmentRef,
            TypeOfProjectionRef,
            TypeOfFeatureRef,
            TypeOfLinkSequenceRef,
            TypeOfOrganisationPartRef,
            TypeOfOrganisationRef,
            TypeOfPlaceRef,
            TypeOfTransferRef,
            TypeOfZoneRef,
            TypeOfLinkRef,
            TypeOfPointRef,
            TypeOfLineRef,
            TypeOfValidityRef,
            TypeOfFrameRef,
            DataSourceRef,
            VersionRef,
            VersionOfObjectRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RepeatedTripFareRequestRef",
                    "type": RepeatedTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleTripFareRequestRef",
                    "type": SingleTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareRequestRef",
                    "type": FareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopFinderRequestRef",
                    "type": StopFinderRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopEventRequestRef",
                    "type": StopEventRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduleRequestRef",
                    "type": ScheduleRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripPlanRequestRef",
                    "type": TripPlanRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResidentialQualificationEligibilityRef",
                    "type": ResidentialQualificationEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibilityRef",
                    "type": CommercialProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibilityRef",
                    "type": UserProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerEligibilityRef",
                    "type": CustomerEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountRef",
                    "type": CustomerAccountRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractRef",
                    "type": FareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerRef",
                    "type": CustomerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTimeAtStopPointRef",
                    "type": StartTimeAtStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResidentialQualificationRef",
                    "type": ResidentialQualificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcessionRef",
                    "type": TypeOfConcessionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameterRef",
                    "type": TypeOfUsageParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffObjectRef",
                    "type": TariffObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareTableRef",
                    "type": TypeOfFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRowRef",
                    "type": FareTableRowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableColumnRef",
                    "type": FareTableColumnRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitRef",
                    "type": TimeUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitRef",
                    "type": GeographicalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequenceRef",
                    "type": FareStructureElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElementRef",
                    "type": CustomerPurchasePackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementRef",
                    "type": ControllableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementRef",
                    "type": ValidableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGivenRef",
                    "type": SalesOfferPackageEntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequiredRef",
                    "type": SalesOfferPackageEntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStayRef",
                    "type": MinimumStayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangingRef",
                    "type": InterchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUseRef",
                    "type": FrequencyOfUseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SuspendingRef",
                    "type": SuspendingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriodRef",
                    "type": UsageValidityPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimitRef",
                    "type": StepLimitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingRef",
                    "type": RoutingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTripRef",
                    "type": RoundTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowanceRef",
                    "type": LuggageAllowanceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGivenRef",
                    "type": EntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequiredRef",
                    "type": EntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicyRef",
                    "type": EligibilityChangePolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicketRef",
                    "type": GroupTicketRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileRef",
                    "type": CommercialProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ProfileParameterRef",
                    "type": ProfileParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SubscribingRef",
                    "type": SubscribingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicyRef",
                    "type": PenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicyRef",
                    "type": ChargingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferabilityRef",
                    "type": TransferabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReplacingRef",
                    "type": ReplacingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefundingRef",
                    "type": RefundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangingRef",
                    "type": ExchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResellingRef",
                    "type": ResellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CancellingRef",
                    "type": CancellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReservingRef",
                    "type": ReservingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindowRef",
                    "type": PurchaseWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElementRef",
                    "type": SalesOfferPackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageRef",
                    "type": SalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementInverseRef",
                    "type": DistanceMatrixElementInverseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementRef",
                    "type": FareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodRef",
                    "type": FulfilmentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintRef",
                    "type": SeriesConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRuleRef",
                    "type": CappingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalRef",
                    "type": TimeIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBandRef",
                    "type": ParkingChargeBandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactorRef",
                    "type": TimeStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceableObjectRef",
                    "type": PriceableObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonthValidityOffsetRef",
                    "type": MonthValidityOffsetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "PricingServiceRef",
                    "type": PricingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundingStepRef",
                    "type": RoundingStepRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundingRef",
                    "type": RoundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingParameterSetRef",
                    "type": PricingParameterSetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplyContractRef",
                    "type": SupplyContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServicePropertiesRef",
                    "type": FlexibleServicePropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripTimeRef",
                    "type": DriverTripTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripRef",
                    "type": DriverTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyPartRef",
                    "type": DutyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccountableElementRef",
                    "type": AccountableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyRef",
                    "type": DutyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefOpportunityRef",
                    "type": ReliefOpportunityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CourseOfJourneysRef",
                    "type": CourseOfJourneysRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverRef",
                    "type": DriverRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePartRef",
                    "type": VehicleServicePartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServiceRef",
                    "type": VehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundBlockRef",
                    "type": CompoundBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockPartRef",
                    "type": TrainBlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPartRef",
                    "type": BlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartCoupleRef",
                    "type": JourneyPartCoupleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoupledJourneyRef",
                    "type": CoupledJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartRef",
                    "type": JourneyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetabledPassingTimeRef",
                    "type": TimetabledPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EstimatedPassingTimeRef",
                    "type": EstimatedPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ObservedPassingTimeRef",
                    "type": ObservedPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TargetPassingTimeRef",
                    "type": TargetPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeRef",
                    "type": PassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRuleTimingRef",
                    "type": InterchangeRuleTimingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRuleRef",
                    "type": InterchangeRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternInterchangeRef",
                    "type": ServiceJourneyPatternInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchangeRef",
                    "type": ServiceJourneyInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultInterchangeRef",
                    "type": DefaultInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRef",
                    "type": InterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyMeetingRef",
                    "type": JourneyMeetingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingConstraintZoneRef",
                    "type": RoutingConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePositionAlignmentRef",
                    "type": VehiclePositionAlignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleQuayAlignmentRef",
                    "type": VehicleQuayAlignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogicalDisplayRef",
                    "type": LogicalDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPropertiesRef",
                    "type": ParkingPropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingCapacityRef",
                    "type": ParkingCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineNetworkRef",
                    "type": LineNetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteInstructionRef",
                    "type": RouteInstructionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LevelRef",
                    "type": LevelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexiblePointPropertiesRef",
                    "type": FlexiblePointPropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLinkPropertiesRef",
                    "type": FlexibleLinkPropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandProfileRef",
                    "type": TimeDemandProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypePreferenceRef",
                    "type": VehicleTypePreferenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternHeadwayRef",
                    "type": JourneyPatternHeadwayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternLayoverRef",
                    "type": JourneyPatternLayoverRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRunTimeRef",
                    "type": JourneyPatternRunTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternWaitTimeRef",
                    "type": JourneyPatternWaitTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultServiceJourneyTimeRef",
                    "type": DefaultServiceJourneyTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultDeadRunRunTimeRef",
                    "type": DefaultDeadRunRunTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TurnaroundTimeLimitTimeRef",
                    "type": TurnaroundTimeLimitTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyTimingRef",
                    "type": JourneyTimingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrewBaseRef",
                    "type": CrewBaseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSeatRef",
                    "type": PassengerSeatRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartmentRef",
                    "type": OperatingDepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperationalContextRef",
                    "type": OperationalContextRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElementRef",
                    "type": TrainElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainInCompoundTrainRef",
                    "type": TrainInCompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentSecurityListingRef",
                    "type": TravelDocumentSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDeviceSecurityListingRef",
                    "type": RetailDeviceSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountSecurityListingRef",
                    "type": CustomerAccountSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractSecurityListingRef",
                    "type": FareContractSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerSecurityListingRef",
                    "type": CustomerSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SchematicMapMemberRef",
                    "type": SchematicMapMemberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SchematicMapRef",
                    "type": SchematicMapRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeliveryVariantRef",
                    "type": DeliveryVariantRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeRef",
                    "type": NoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfileRef",
                    "type": VehicleEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleModelRef",
                    "type": VehicleModelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRef",
                    "type": VehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCapacityRef",
                    "type": PassengerCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilityRequirementRef",
                    "type": FacilityRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleManoeuvringRequirementRef",
                    "type": VehicleManoeuvringRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRequirementRef",
                    "type": VehicleRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "OnboardStayRef",
                    "type": OnboardStayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccommodationRef",
                    "type": AccommodationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "FacilityRef",
                    "type": FacilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModeRef",
                    "type": ModeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SubmodeRef",
                    "type": SubmodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OpenTransportModeRef",
                    "type": OpenTransportModeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicProjectionRef",
                    "type": TopographicProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjectionRef",
                    "type": ComplexFeatureProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjectionRef",
                    "type": LinkSequenceProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjectionRef",
                    "type": ZoneProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjectionRef",
                    "type": LinkProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjectionRef",
                    "type": PointProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPatternRef",
                    "type": TimingPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceRef",
                    "type": LinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionRef",
                    "type": SalesTransactionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecificationRef",
                    "type": OfferedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecificationRef",
                    "type": RequestedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecificationRef",
                    "type": TravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntryRef",
                    "type": FareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogEntryRef",
                    "type": LogEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeNameRef",
                    "type": AlternativeNameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnectionRef",
                    "type": DefaultConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnectionRef",
                    "type": SiteConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionRef",
                    "type": ConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRef",
                    "type": AccessRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ServiceLinkRef",
                    "type": ServiceLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRef",
                    "type": LineLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRef",
                    "type": RouteLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRef",
                    "type": WireLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRef",
                    "type": RoadLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRef",
                    "type": RailwayLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRef",
                    "type": ActivationLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePointRef",
                    "type": RoutePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WirePointRef",
                    "type": WirePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadPointRef",
                    "type": RoadPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayPointRef",
                    "type": RailwayPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPointRef",
                    "type": TrafficControlPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPointRef",
                    "type": BeaconPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPointRef",
                    "type": ActivationPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointRef",
                    "type": PointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarRef",
                    "type": ServiceCalendarRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeTextRef",
                    "type": AlternativeTextRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameterRef",
                    "type": ValidityRuleParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTriggerRef",
                    "type": ValidityTriggerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityConditionRef",
                    "type": ValidityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilityRoleRef",
                    "type": ResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentreRef",
                    "type": ControlCentreRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnitRef",
                    "type": OrganisationalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartmentRef",
                    "type": DepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPartRef",
                    "type": OrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllAuthoritiesRef",
                    "type": AllAuthoritiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOperatorsRef",
                    "type": AllOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllTransportOrganisationsRef",
                    "type": AllTransportOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOrganisationsRef",
                    "type": AllOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilitySetRef",
                    "type": ResponsibilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayVariantRef",
                    "type": DestinationDisplayVariantRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirectionRef",
                    "type": AllowedLineDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GroupOfCustomerPurchasePackagesRef",
                    "type": GroupOfCustomerPurchasePackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroupRef",
                    "type": PriceGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroupRef",
                    "type": RhythmicalJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroupRef",
                    "type": HeadwayJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyFrequencyGroupRef",
                    "type": JourneyFrequencyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServicesRef",
                    "type": GroupOfServicesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfStopPlacesRef",
                    "type": GroupOfStopPlacesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestHierarchyRef",
                    "type": PointOfInterestHierarchyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimingLinksRef",
                    "type": GroupOfTimingLinksRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPlacesRef",
                    "type": GroupOfPlacesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParentSectionRef",
                    "type": ParentSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParentCommonSectionRef",
                    "type": ParentCommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSectionRef",
                    "type": CommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSectionRef",
                    "type": LineSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareSectionRef",
                    "type": FareSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSectionRef",
                    "type": GeneralSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SectionRef",
                    "type": SectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogRef",
                    "type": LogRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebandsRef",
                    "type": GroupOfTimebandsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceRef",
                    "type": PlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LayerRef",
                    "type": LayerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GeneralGroupOfEntitiesRef",
                    "type": GeneralGroupOfEntitiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrameRef",
                    "type": SalesTransactionFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrameRef",
                    "type": FareFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrameRef",
                    "type": ServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrameRef",
                    "type": DriverScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrameRef",
                    "type": VehicleScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrameRef",
                    "type": TimetableFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrameRef",
                    "type": SiteFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrameRef",
                    "type": InfrastructureFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrameRef",
                    "type": GeneralFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrameRef",
                    "type": ResourceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrameRef",
                    "type": ServiceCalendarFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrameRef",
                    "type": CompositeFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingMomentRef",
                    "type": ChargingMomentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnitRef",
                    "type": PriceUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfJourneyPartitionRef",
                    "type": PurposeOfJourneyPartitionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingAlgorithmTypeRef",
                    "type": TimingAlgorithmTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassificationRef",
                    "type": PointOfInterestClassificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionRef",
                    "type": DirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivationRef",
                    "type": TypeOfActivationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfEquipmentProfileRef",
                    "type": PurposeOfEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProductCategoryRef",
                    "type": TypeOfProductCategoryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPaymentMethodRef",
                    "type": TypeOfPaymentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassOfUseRef",
                    "type": ClassOfUseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperationRef",
                    "type": TypeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCodespaceAssignmentRef",
                    "type": TypeOfCodespaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BrandingRef",
                    "type": BrandingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRoleRef",
                    "type": TypeOfResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfGroupingRef",
                    "type": PurposeOfGroupingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDeviceRef",
                    "type": TypeOfRetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatusRef",
                    "type": CustomerAccountStatusRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccountRef",
                    "type": TypeOfCustomerAccountRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntryRef",
                    "type": TypeOfFareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractRef",
                    "type": TypeOfFareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignmentRef",
                    "type": TypeOfAccessRightAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackageRef",
                    "type": TypeOfSalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElementRef",
                    "type": TypeOfFareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariffRef",
                    "type": TypeOfTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllDistributionChannelsRef",
                    "type": AllDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMachineReadabilityRef",
                    "type": TypeOfMachineReadabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocumentRef",
                    "type": TypeOfTravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactorRef",
                    "type": TypeOfFareStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPricingRuleRef",
                    "type": TypeOfPricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleServiceRef",
                    "type": TypeOfFlexibleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipmentRef",
                    "type": TypeOfPassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceFeatureRef",
                    "type": TypeOfServiceFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestionRef",
                    "type": TypeOfCongestionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandTypeRef",
                    "type": TypeOfTimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPatternRef",
                    "type": TypeOfJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityListRef",
                    "type": TypeOfSecurityListRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariantRef",
                    "type": TypeOfDeliveryVariantRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNoticeRef",
                    "type": TypeOfNoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceRef",
                    "type": TypeOfServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacilityRef",
                    "type": TypeOfFacilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipmentRef",
                    "type": TypeOfEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjectionRef",
                    "type": TypeOfProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeatureRef",
                    "type": TypeOfFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequenceRef",
                    "type": TypeOfLinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPartRef",
                    "type": TypeOfOrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationRef",
                    "type": TypeOfOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlaceRef",
                    "type": TypeOfPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransferRef",
                    "type": TypeOfTransferRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZoneRef",
                    "type": TypeOfZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkRef",
                    "type": TypeOfLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPointRef",
                    "type": TypeOfPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLineRef",
                    "type": TypeOfLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfValidityRef",
                    "type": TypeOfValidityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrameRef",
                    "type": TypeOfFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DataSourceRef",
                    "type": DataSourceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VersionRef",
                    "type": VersionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VersionOfObjectRef",
                    "type": VersionOfObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
