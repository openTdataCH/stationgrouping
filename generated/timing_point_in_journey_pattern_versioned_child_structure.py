from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from generated.border_point_ref import BorderPointRef
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.garage_point_ref import GaragePointRef
from generated.journey_pattern_headways_rel_structure import (
    JourneyPatternHeadwaysRelStructure,
)
from generated.journey_pattern_wait_times_rel_structure import (
    JourneyPatternWaitTimesRelStructure,
)
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.parking_point_ref import ParkingPointRef
from generated.point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)
from generated.relief_point_ref import ReliefPointRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.timing_link_ref_structure import TimingLinkRefStructure
from generated.timing_point_ref import TimingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPointInJourneyPatternVersionedChildStructure(
    PointInLinkSequenceVersionedChildStructure
):
    """
    Type for TIMING POINT IN JOURNEY PATTERN.

    :ivar choice_1:
    :ivar onward_timing_link_ref: Used to disambiguate if multiple links
        between the same points.
    :ivar is_wait_point: Whether point is a wait point.
    :ivar wait_time_or_wait_times:
    :ivar headways: Wait times for TIMING POINT. There may be different
        times for different time demands.
    :ivar notice_assignments: NOTICEs for TIMING POINT IN JOURNEY
        PATTERN.
    """

    class Meta:
        name = "TimingPointInJourneyPattern_VersionedChildStructure"

    choice_1: Optional[
        Union[
            BorderPointRef,
            FareScheduledStopPointRef,
            ScheduledStopPointRef,
            GaragePointRef,
            ParkingPointRef,
            ReliefPointRef,
            TimingPointRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    onward_timing_link_ref: Optional[TimingLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_wait_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWaitPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_time_or_wait_times: Optional[
        Union[XmlDuration, JourneyPatternWaitTimesRelStructure]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WaitTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "waitTimes",
                    "type": JourneyPatternWaitTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
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
