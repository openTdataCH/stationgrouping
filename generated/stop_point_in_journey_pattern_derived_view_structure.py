from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from generated.derived_view_structure import DerivedViewStructure
from generated.fare_point_in_pattern_ref import FarePointInPatternRef
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.onward_service_link_view import OnwardServiceLinkView
from generated.onward_timing_link_view import OnwardTimingLinkView
from generated.point_in_journey_pattern_ref import PointInJourneyPatternRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.scheduled_stop_point_view import ScheduledStopPointView
from generated.service_link_ref_structure import ServiceLinkRefStructure
from generated.stop_point_in_journey_pattern_ref import (
    StopPointInJourneyPatternRef,
)
from generated.time_demand_type_ref import TimeDemandTypeRef
from generated.timeband_ref import TimebandRef
from generated.timing_point_in_journey_pattern_ref import (
    TimingPointInJourneyPatternRef,
)
from generated.timing_point_status_enumeration import (
    TimingPointStatusEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPointInJourneyPatternDerivedViewStructure(DerivedViewStructure):
    """
    Type for STOP POINT IN JOURNEY PATTERN VIEW.

    :ivar choice:
    :ivar visit_number: Count of number of visits to this stop - as per
        SIRI use. Default is 1
    :ivar
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view:
    :ivar onward_timing_link_view:
    :ivar onward_service_link_ref_or_onward_service_link_view:
    :ivar timing_point_status: Nature of TIMING POINT. Default is
        primary.
    :ivar is_wait_point: Whether point is a wait point.
    :ivar time_demand_type_ref_or_timeband_ref:
    :ivar wait_time: Wait time as interval. OPTIMISATION assuming
        default Time Demand. Use this to declare a single time. on a
        specific journey Other wise a list of times for different time
        demands for a JOURNEY PATTERN used in many different times.
    :ivar scheduled_headway_interval: Scheduled normal headway interval.
    :ivar minimum_headway_interval: Minimum headway interval.
    :ivar maximum_headway_interval: Maximum headway interval.
    :ivar order: Order of CALL within Journey.
    """

    class Meta:
        name = "StopPointInJourneyPattern_DerivedViewStructure"

    choice: Optional[
        Union[
            FarePointInPatternRef,
            StopPointInJourneyPatternRef,
            TimingPointInJourneyPatternRef,
            PointInJourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FarePointInPatternRef",
                    "type": FarePointInPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPatternRef",
                    "type": StopPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPatternRef",
                    "type": TimingPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPatternRef",
                    "type": PointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view: Optional[
        Union[
            FareScheduledStopPointRef,
            ScheduledStopPointRef,
            ScheduledStopPointView,
        ]
    ] = field(
        default=None,
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
                {
                    "name": "ScheduledStopPointView",
                    "type": ScheduledStopPointView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    onward_timing_link_view: Optional[OnwardTimingLinkView] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onward_service_link_ref_or_onward_service_link_view: Optional[
        Union[ServiceLinkRefStructure, OnwardServiceLinkView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnwardServiceLinkRef",
                    "type": ServiceLinkRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardServiceLinkView",
                    "type": OnwardServiceLinkView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    timing_point_status: Optional[TimingPointStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "TimingPointStatus",
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
    wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
