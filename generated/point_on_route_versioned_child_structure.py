from dataclasses import dataclass, field
from typing import Optional, Union

from generated.activation_point_ref import ActivationPointRef
from generated.beacon_point_ref import BeaconPointRef
from generated.border_point_ref import BorderPointRef
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.garage_point_ref import GaragePointRef
from generated.parking_point_ref import ParkingPointRef
from generated.point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)
from generated.point_ref import PointRef
from generated.railway_point_ref import RailwayPointRef
from generated.relief_point_ref import ReliefPointRef
from generated.road_point_ref import RoadPointRef
from generated.route_instructions_rel_structure import (
    RouteInstructionsRelStructure,
)
from generated.route_link_ref_structure import RouteLinkRefStructure
from generated.route_point_ref import RoutePointRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.timing_point_ref import TimingPointRef
from generated.traffic_control_point_ref import TrafficControlPointRef
from generated.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnRouteVersionedChildStructure(
    PointInLinkSequenceVersionedChildStructure
):
    """
    Type for a POINT ON ROUTE.

    :ivar choice_1:
    :ivar onward_route_link_ref: Optional Reference to onward link to
        use - can be used to disambiguate where there are multiple links
        between the same point.
    :ivar route_instructions: Instructins for following route. +v1.1
    """

    class Meta:
        name = "PointOnRoute_VersionedChildStructure"

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
            ),
        },
    )
    onward_route_link_ref: Optional[RouteLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardRouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_instructions: Optional[RouteInstructionsRelStructure] = field(
        default=None,
        metadata={
            "name": "routeInstructions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
