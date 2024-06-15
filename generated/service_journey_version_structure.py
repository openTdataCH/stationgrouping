from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from generated.block_ref import BlockRef
from generated.calls_rel_structure import CallsRelStructure
from generated.check_constraints_rel_structure import (
    CheckConstraintsRelStructure,
)
from generated.compound_train_ref import CompoundTrainRef
from generated.course_of_journeys_ref import CourseOfJourneysRef
from generated.day_type_refs_rel_structure import DayTypeRefsRelStructure
from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.direction_type import DirectionType
from generated.dynamic_advertisement_enumeration import (
    DynamicAdvertisementEnumeration,
)
from generated.flexible_line_ref import FlexibleLineRef
from generated.flexible_line_view import FlexibleLineView
from generated.flexible_service_properties import FlexibleServiceProperties
from generated.flexible_service_properties_ref import (
    FlexibleServicePropertiesRef,
)
from generated.frequency_structure import FrequencyStructure
from generated.group_of_services_refs_rel_structure import (
    GroupOfServicesRefsRelStructure,
)
from generated.headway_journey_group_ref import HeadwayJourneyGroupRef
from generated.journey_endpoint_structure import JourneyEndpointStructure
from generated.journey_frequency_group_ref import JourneyFrequencyGroupRef
from generated.journey_parts_rel_structure import JourneyPartsRelStructure
from generated.journey_pattern_ref import JourneyPatternRef
from generated.journey_pattern_view import JourneyPatternView
from generated.journey_version_structure import JourneyVersionStructure
from generated.line_ref import LineRef
from generated.line_view import LineView
from generated.operational_context_ref import OperationalContextRef
from generated.operator_ref import OperatorRef
from generated.operator_view import OperatorView
from generated.passenger_carrying_requirement_ref import (
    PassengerCarryingRequirementRef,
)
from generated.passenger_carrying_requirements_view import (
    PassengerCarryingRequirementsView,
)
from generated.rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from generated.route_ref import RouteRef
from generated.service_alteration_enumeration import (
    ServiceAlterationEnumeration,
)
from generated.service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_pattern_ref import ServicePatternRef
from generated.time_demand_type_ref_structure import TimeDemandTypeRefStructure
from generated.time_demand_type_refs_rel_structure import (
    TimeDemandTypeRefsRelStructure,
)
from generated.timetabled_passing_times_rel_structure import (
    TimetabledPassingTimesRelStructure,
)
from generated.timing_algorithm_type_ref import TimingAlgorithmTypeRef
from generated.train_block_ref import TrainBlockRef
from generated.train_number_refs_rel_structure import (
    TrainNumberRefsRelStructure,
)
from generated.train_ref import TrainRef
from generated.train_size import TrainSize
from generated.vehicle_equipments_rel_structure import (
    VehicleEquipmentsRelStructure,
)
from generated.vehicle_journey_layovers_rel_structure import (
    VehicleJourneyLayoversRelStructure,
)
from generated.vehicle_journey_run_times_rel_structure import (
    VehicleJourneyRunTimesRelStructure,
)
from generated.vehicle_journey_wait_times_rel_structure import (
    VehicleJourneyWaitTimesRelStructure,
)
from generated.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyVersionStructure(JourneyVersionStructure):
    """
    Data type for a planned VEHICLE JOURNEY (Production Timetable Service).

    :ivar service_alteration: Whether journey is as planned, a
        cancellation or an extra journey.  Default is as Planned.
    :ivar departure_time: Time of departure.
    :ivar departure_day_offset: Day offset if day of departure time of
        VEHICLE JOURNEY differs from the current OPERATING DAY.
    :ivar frequency: Frequency of Journey.
    :ivar journey_duration: Total length of Journey. Can be computed
        from individual times.  Add to Departure time to obtain JOURNEY
        arrival time.
    :ivar day_types: DAY TYPEs for Journey.
    :ivar route_ref:
    :ivar choice:
    :ivar time_demand_type_ref: Reference to a TIME DEMAND TYPE used at
        start of JOURNEY.
    :ivar timing_algorithm_type_ref:
    :ivar
        rhythmical_journey_group_ref_or_headway_journey_group_ref_or_journey_frequency_group_ref:
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    :ivar operational_context_ref:
    :ivar train_block_ref_or_block_ref:
    :ivar course_of_journeys_ref:
    :ivar public_code: Public code for JOURNEY.
    :ivar operator_ref_or_operator_view:
    :ivar choice_1:
    :ivar direction_type:
    :ivar journey_pattern_view:
    :ivar groups_of_services: Grouping of services  of a journey - for a
        multi-part journey only.
    :ivar time_demand_types: Other TIME DEMAND TYPEs used in journey.
    :ivar train_numbers: TRAIN NUMBERs -= derived through JOURNEY PARTs
        of a journey - for a multi-part journey only.
    :ivar origin: Origin  for JOURNEY.
    :ivar destination: Destination  for JOURNEY.
    :ivar print: Whether the journey is included in printed media.
        Default is true.
    :ivar dynamic: When SERVICE JOURNEY is to be publicised in dynamic
        media. Default is always.
    :ivar wait_times: WAIT TIMEs for VEHICLE JOURNEY at different TIMING
        POINTs.
    :ivar run_times: Run times for VEHICLE JOURNEY over different TIMING
        LINKs.
    :ivar layovers: LAYOVER times for VEHICLE JOURNEY.
    :ivar passing_times: PASSING TIMEs  for VEHICLE JOURNEY.
    :ivar parts: JOURNEY PARTs of a journey - for a multi-part journey
        only.
    :ivar calls: Complete sequence of stops along the route path, in
        calling order.
    :ivar facilities: FACILITies available associated with JOURNEY.
    :ivar check_constraints: CHECK CONSTRAINTs  which apply to SERVICE
        JOURNEY, e.g. check in time, security time. These are advisory
        only and not for use in  journey planning.
    :ivar
        passenger_carrying_requirement_ref_or_passenger_carrying_requirements_view:
    :ivar train_size:
    :ivar equipments: VEHICLE EQUIPMENT available on service.
    :ivar
        flexible_service_properties_ref_or_flexible_service_properties:
    """

    class Meta:
        name = "ServiceJourney_VersionStructure"

    service_alteration: Optional[ServiceAlterationEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceAlteration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency: Optional[FrequencyStructure] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    time_demand_type_ref: Optional[TimeDemandTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_algorithm_type_ref: Optional[TimingAlgorithmTypeRef] = field(
        default=None,
        metadata={
            "name": "TimingAlgorithmTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rhythmical_journey_group_ref_or_headway_journey_group_ref_or_journey_frequency_group_ref: Optional[
        Union[
            RhythmicalJourneyGroupRef,
            HeadwayJourneyGroupRef,
            JourneyFrequencyGroupRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default=None,
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
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_block_ref_or_block_ref: Optional[Union[TrainBlockRef, BlockRef]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
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
                ),
            },
        )
    )
    course_of_journeys_ref: Optional[CourseOfJourneysRef] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_ref_or_operator_view: Optional[
        Union[OperatorRef, OperatorView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorView",
                    "type": OperatorView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[FlexibleLineRef, LineRef, LineView, FlexibleLineView]
    ] = field(
        default=None,
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
                {
                    "name": "LineView",
                    "type": LineView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLineView",
                    "type": FlexibleLineView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_type: Optional[DirectionType] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_pattern_view: Optional[JourneyPatternView] = field(
        default=None,
        metadata={
            "name": "JourneyPatternView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_services: Optional[GroupOfServicesRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_types: Optional[TimeDemandTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_numbers: Optional[TrainNumberRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    origin: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: Optional[JourneyEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: Optional[VehicleJourneyWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_times: Optional[VehicleJourneyRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: Optional[VehicleJourneyLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passing_times: Optional[TimetabledPassingTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "passingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parts: Optional[JourneyPartsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    calls: Optional[CallsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraints: Optional[CheckConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_carrying_requirement_ref_or_passenger_carrying_requirements_view: Optional[
        Union[
            PassengerCarryingRequirementRef, PassengerCarryingRequirementsView
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementsView",
                    "type": PassengerCarryingRequirementsView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_size: Optional[TrainSize] = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipments: Optional[VehicleEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_service_properties_ref_or_flexible_service_properties: Optional[
        Union[FlexibleServicePropertiesRef, FlexibleServiceProperties]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleServicePropertiesRef",
                    "type": FlexibleServicePropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServiceProperties",
                    "type": FlexibleServiceProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
