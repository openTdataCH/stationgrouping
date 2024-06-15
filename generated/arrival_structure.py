from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlTime

from generated.accessibility_assessment import AccessibilityAssessment
from generated.check_constraint import CheckConstraint
from generated.duty_part_ref import DutyPartRef
from generated.dynamic_stop_assignment import DynamicStopAssignment
from generated.dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from generated.interchange_rules_rel_structure import (
    InterchangeRulesRelStructure,
)
from generated.journey_meeting_views_rel_structure import (
    JourneyMeetingViewsRelStructure,
)
from generated.journey_part_ref import JourneyPartRef
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from generated.quay_assignment_view import QuayAssignmentView
from generated.service_journey_interchanges_rel_structure import (
    ServiceJourneyInterchangesRelStructure,
)
from generated.time_demand_type_ref import TimeDemandTypeRef
from generated.timeband_ref import TimebandRef
from generated.vehicle_journey_stop_assignment_ref import (
    VehicleJourneyStopAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ArrivalStructure:
    """
    Reorganisation  of Passing times as arrival.

    :ivar time: Latest Arrival time.
    :ivar day_offset: Number of days after the starting  day of the
        journey. Default is 0 for same day.
    :ivar for_alighting: Whether  alighting is allowed at the stop
        Default is true.
    :ivar is_flexible: Whether use of stop is flexible, i.e. requires
        phoning to arrange. Must be a  FLEXIBLE LINE.  Default is false.
    :ivar journey_part_ref:
    :ivar journey_meetings: JOURNEY MEETINGs for visit.
    :ivar interchanges: INTERCHANGEs for visit.
    :ivar interchange_rules: INTERCHANGE RULEs for visit.
    :ivar time_demand_type_ref_or_timeband_ref:
    :ivar duty_part_ref:
    :ivar choice:
    :ivar dynamic_stop_assignment:
    :ivar accessibility_assessment:
    :ivar check_constraint:
    :ivar notice_assignments: NOTICEs of a CALL that apply only to the
        Arrival  or departure.
    """

    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_alighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_flexible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFlexible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_ref: Optional[JourneyPartRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_meetings: Optional[JourneyMeetingViewsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyMeetings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    interchanges: Optional[ServiceJourneyInterchangesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    interchange_rules: Optional[InterchangeRulesRelStructure] = field(
        default=None,
        metadata={
            "name": "interchangeRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_ref_or_timeband_ref: Optional[
        Union[TimeDemandTypeRef, TimebandRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    duty_part_ref: Optional[DutyPartRef] = field(
        default=None,
        metadata={
            "name": "DutyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            VehicleJourneyStopAssignmentRef,
            DynamicStopAssignmentRef,
            PassengerStopAssignmentRef,
            QuayAssignmentView,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayAssignmentView",
                    "type": QuayAssignmentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    dynamic_stop_assignment: Optional[DynamicStopAssignment] = field(
        default=None,
        metadata={
            "name": "DynamicStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraint: Optional[CheckConstraint] = field(
        default=None,
        metadata={
            "name": "CheckConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
