from dataclasses import dataclass, field
from typing import Optional, Union

from generated.activation_point_ref import ActivationPointRef
from generated.beacon_point_ref import BeaconPointRef
from generated.booking_arrangements_structure import (
    BookingArrangementsStructure,
)
from generated.border_point_ref import BorderPointRef
from generated.dead_run_call_part_structure import DeadRunCallPartStructure
from generated.destination_display_ref import DestinationDisplayRef
from generated.destination_display_view import DestinationDisplayView
from generated.dynamic_advertisement_enumeration import (
    DynamicAdvertisementEnumeration,
)
from generated.entity_in_version_structure import VersionedChildStructure
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.flexible_point_properties import FlexiblePointProperties
from generated.garage_point_ref import GaragePointRef
from generated.multilingual_string import MultilingualString
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.parking_point_ref import ParkingPointRef
from generated.point_in_journey_pattern_ref_structure import (
    PointInJourneyPatternRefStructure,
)
from generated.point_ref import PointRef
from generated.railway_point_ref import RailwayPointRef
from generated.relief_point_ref import ReliefPointRef
from generated.request_method_type_enumeration import (
    RequestMethodTypeEnumeration,
)
from generated.road_point_ref import RoadPointRef
from generated.route_point_ref import RoutePointRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.scheduled_stop_point_view import ScheduledStopPointView
from generated.stop_use_enumeration import StopUseEnumeration
from generated.timing_point_ref import TimingPointRef
from generated.traffic_control_point_ref import TrafficControlPointRef
from generated.vias_rel_structure import ViasRelStructure
from generated.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunCallVersionedChildStructure(VersionedChildStructure):
    """
    Data type for DEAD RUN CALL.

    :ivar choice:
    :ivar point_in_journey_pattern_ref: Point in JOURNEY PATTERN upon
        which this DEAD RUN CALL is based. Can be used to obtain full
        association sets.
    :ivar arrival: Arrival at DEAD RUN CALL.
    :ivar departure: Departure from a DEAD RUN CALL.
    :ivar destination_display_ref_or_destination_display_view:
    :ivar vias: Destinations that the SERVICE goes via.
    :ivar flexible_point_properties:
    :ivar change_of_destination_display: Whether DESTINATION DISPLAY
        should be updated at this point. If DESTINATION NAME value is
        different from Previous stop this is implicit.
    :ivar change_of_service_requirements: Whether Service Requirements
        Change at this point.
    :ivar notice_assignments: NOTICEs for POINT IN JOURNEY PATTERN.
    :ivar request_stop: Whether stop is a request stop for this journey.
        Default is false.
    :ivar request_method: Method to Request Stop in this particular
        service pattern; if none specified, as as per stop.  +V1.1
    :ivar stop_use: Nature of use of stop, e.g. access, interchange
        only, or pass through. Default is Access.
    :ivar booking_arrangements: Booking Arrangements for stop if
        different from those for SERVICE JOURNEY.
    :ivar print: Whether the stop is included in printed media. Default
        is true. +v1.1
    :ivar dynamic: When STOP POINT IN JOURNEY PATTERN is to be
        publicised in dynamic media. Default is always. +v1.1
    :ivar note: Text annotation that applies to this DEAD RUN CALL. This
        is for internal use. Customer facing should be added to
        footnote.
    :ivar order: Order of DEAD RUN CALL within Journey.
    """

    class Meta:
        name = "DeadRunCall_VersionedChildStructure"

    choice: Optional[
        Union[
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
            ScheduledStopPointView,
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
                    "name": "ScheduledStopPointView",
                    "type": ScheduledStopPointView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    point_in_journey_pattern_ref: Optional[
        PointInJourneyPatternRefStructure
    ] = field(
        default=None,
        metadata={
            "name": "PointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    arrival: Optional[DeadRunCallPartStructure] = field(
        default=None,
        metadata={
            "name": "Arrival",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure: Optional[DeadRunCallPartStructure] = field(
        default=None,
        metadata={
            "name": "Departure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_ref_or_destination_display_view: Optional[
        Union[DestinationDisplayRef, DestinationDisplayView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vias: Optional[ViasRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_point_properties: Optional[FlexiblePointProperties] = field(
        default=None,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    change_of_destination_display: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfDestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    change_of_service_requirements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfServiceRequirements",
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
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_method: Optional[RequestMethodTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RequestMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_use: Optional[StopUseEnumeration] = field(
        default=None,
        metadata={
            "name": "StopUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
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
    note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Note",
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
