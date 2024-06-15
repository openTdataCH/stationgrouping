from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from generated.block_ref import BlockRef
from generated.compound_train_ref import CompoundTrainRef
from generated.course_of_journeys_ref import CourseOfJourneysRef
from generated.day_type_refs_rel_structure import DayTypeRefsRelStructure
from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.frequency_structure import FrequencyStructure
from generated.headway_journey_group_ref import HeadwayJourneyGroupRef
from generated.journey_frequency_group_ref import JourneyFrequencyGroupRef
from generated.journey_parts_rel_structure import JourneyPartsRelStructure
from generated.journey_pattern_ref import JourneyPatternRef
from generated.journey_version_structure import JourneyVersionStructure
from generated.operational_context_ref import OperationalContextRef
from generated.rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from generated.route_ref import RouteRef
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
from generated.train_component_label_assignments_rel_structure import (
    TrainComponentLabelAssignmentsRelStructure,
)
from generated.train_ref import TrainRef
from generated.vehicle_journey_layovers_rel_structure import (
    VehicleJourneyLayoversRelStructure,
)
from generated.vehicle_journey_run_times_rel_structure import (
    VehicleJourneyRunTimesRelStructure,
)
from generated.vehicle_journey_stop_assignments_rel_structure import (
    VehicleJourneyStopAssignmentsRelStructure,
)
from generated.vehicle_journey_wait_times_rel_structure import (
    VehicleJourneyWaitTimesRelStructure,
)
from generated.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyVersionStructure(JourneyVersionStructure):
    """
    Type for VEHICLE JOURNEY.

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
    :ivar time_demand_types: Other TIME DEMAND TYPEs used in JOURNEY.
    :ivar parts: JOURNEY PARTs  of a JOURNEY - for a multi part JOURNEY
        only.
    :ivar train_component_label_assignments: Labelling of carriages for
        Train associated with JOURNEY.
    :ivar vehicle_journey_stop_assignments: Niormal  VEHICLE STOP
        ASSIGNMENTs  for VEHICLE JOURNEY, +v1.1
    :ivar wait_times: WAIT TIMEs for VEHICLE JOURNEY at different TIMING
        POINTs.
    :ivar run_times: Run times for VEHICLE JOURNEY over different TIMING
        LINKs.
    :ivar layovers: LAYOVER times for VEHICLE JOURNEY.
    :ivar passing_times: PASSING TIMEs  for VEHICLE JOURNEY.
    """

    class Meta:
        name = "VehicleJourney_VersionStructure"

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
    time_demand_types: Optional[TimeDemandTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
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
    train_component_label_assignments: Optional[
        TrainComponentLabelAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "trainComponentLabelAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_journey_stop_assignments: Optional[
        VehicleJourneyStopAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleJourneyStopAssignments",
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
