from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlTime

from generated.connecting_journey_view import ConnectingJourneyView
from generated.connection_ref_structure import ConnectionRefStructure
from generated.dated_special_service_ref import DatedSpecialServiceRef
from generated.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from generated.dead_run_ref import DeadRunRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.flexible_line_ref import FlexibleLineRef
from generated.line_derived_view_structure import LineDerivedViewStructure
from generated.line_ref import LineRef
from generated.multilingual_string import MultilingualString
from generated.point_in_journey_pattern_ref_structure import (
    PointInJourneyPatternRefStructure,
)
from generated.reason_for_meeting_enumeration import (
    ReasonForMeetingEnumeration,
)
from generated.scheduled_stop_point_ref_structure import (
    ScheduledStopPointRefStructure,
)
from generated.service_journey_ref import ServiceJourneyRef
from generated.special_service_ref import SpecialServiceRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.vehicle_journey_ref import VehicleJourneyRef
from generated.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingVersionStructure(DataManagedObjectStructure):
    """
    Type for JOURNEY MEETING.

    :ivar name: Name of Journey meeting.
    :ivar at_stop_point_ref: SCHEDULED STOP POINT at which JOURNEY
        MEETING takes place.
    :ivar from_journey_ref: VEHICLE JOURNEY that feeds JOURNEY MEETING.
    :ivar to_journey_ref: VEHICLE JOURNEY  that distributes from JOURNEY
        MEETING.
    :ivar from_point_in_journey_pattern_ref: POINT IN JOURNEY PATTERN
        ofr  feeder  journey JOURNEY PATTERN.
    :ivar to_point_in_journey_pattern_ref: POINT IN JOURNEY PATTERN ofr
        distributorjourney JOURNEY PATTERN.
    :ivar description: Description of JOURNEY MEETING.
    :ivar earliest_time: Earliest time for JOURNEY MEETING.
    :ivar earliest_time_day_offset: Earliest time Day Offset from start
        of FROM JOURNEY.
    :ivar latest_time: Latest time for JOURNEY MEETING.
    :ivar latest_time_day_offset: Latest time Day Offset from start of
        FROM JOURNEY.
    :ivar reason: Reason for JOURNEY MEETING.
    :ivar connection_ref: Reference to CONNECTION at which JOURNEY
        MEETING takes place.
    :ivar connecting_stop_point_ref: SCHEDULED STOP POINT  to which
        JOURNEY MEETING connects if different from current stop
        interchange.
    :ivar connecting_stop_point_name: Name of CONNETCING STOP POINT.
    :ivar choice:
    :ivar flexible_line_ref_or_line_ref_or_connecting_line_view:
    """

    class Meta:
        name = "JourneyMeeting_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    at_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "AtStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_journey_ref: VehicleJourneyRefStructure = field(
        metadata={
            "name": "FromJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_journey_ref: VehicleJourneyRefStructure = field(
        metadata={
            "name": "ToJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    from_point_in_journey_pattern_ref: Optional[
        PointInJourneyPatternRefStructure
    ] = field(
        default=None,
        metadata={
            "name": "FromPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_in_journey_pattern_ref: Optional[
        PointInJourneyPatternRefStructure
    ] = field(
        default=None,
        metadata={
            "name": "ToPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EarliestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "LatestTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reason: Optional[ReasonForMeetingEnumeration] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connection_ref: Optional[ConnectionRefStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connecting_stop_point_ref: List[ScheduledStopPointRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connecting_stop_point_name: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingStopPointName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
            ConnectingJourneyView,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "ConnectingJourneyView",
                    "type": ConnectingJourneyView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    flexible_line_ref_or_line_ref_or_connecting_line_view: Optional[
        Union[FlexibleLineRef, LineRef, LineDerivedViewStructure]
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
                    "name": "ConnectingLineView",
                    "type": LineDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
