from dataclasses import dataclass, field
from typing import Optional, Union

from generated.activation_link_ref import ActivationLinkRef
from generated.activation_point import ActivationPoint
from generated.activation_point_ref import ActivationPointRef
from generated.beacon_point import BeaconPoint
from generated.beacon_point_ref import BeaconPointRef
from generated.border_point import BorderPoint
from generated.border_point_ref import BorderPointRef
from generated.fare_scheduled_stop_point import FareScheduledStopPoint
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.garage_point import GaragePoint
from generated.garage_point_ref import GaragePointRef
from generated.line_link_ref import LineLinkRef
from generated.parking_point import ParkingPoint
from generated.parking_point_ref import ParkingPointRef
from generated.path_junction import PathJunction
from generated.path_link_ref import PathLinkRef
from generated.point_2 import Point2
from generated.point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)
from generated.point_ref import PointRef
from generated.railway_junction import RailwayJunction
from generated.railway_link_ref import RailwayLinkRef
from generated.railway_point_ref import RailwayPointRef
from generated.relief_point import ReliefPoint
from generated.relief_point_ref import ReliefPointRef
from generated.road_junction import RoadJunction
from generated.road_link_ref import RoadLinkRef
from generated.road_point_ref import RoadPointRef
from generated.route_link_ref import RouteLinkRef
from generated.route_point import RoutePoint
from generated.route_point_ref import RoutePointRef
from generated.scheduled_stop_point import ScheduledStopPoint
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.service_link_ref import ServiceLinkRef
from generated.timing_link_ref import TimingLinkRef
from generated.timing_point import TimingPoint
from generated.timing_point_ref import TimingPointRef
from generated.traffic_control_point import TrafficControlPoint
from generated.traffic_control_point_ref import TrafficControlPointRef
from generated.wire_junction import WireJunction
from generated.wire_link_ref import WireLinkRef
from generated.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnSectionVersionedChildStructure(
    PointInLinkSequenceVersionedChildStructure
):
    """
    Type for a POINT on a SECTION.

    :ivar choice_1:
    :ivar choice_2:
    :ivar reverse: Whether link is navigated in to / from, i.e. reverse
        direction . Default is false, i.e. from to.
    """

    class Meta:
        name = "PointOnSection_VersionedChildStructure"

    choice_1: Optional[
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
            ),
        },
    )
    choice_2: Optional[
        Union[
            ServiceLinkRef,
            LineLinkRef,
            PathLinkRef,
            TimingLinkRef,
            RouteLinkRef,
            WireLinkRef,
            RoadLinkRef,
            RailwayLinkRef,
            ActivationLinkRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
