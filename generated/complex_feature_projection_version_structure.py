from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.activation_point_ref import ActivationPointRef
from generated.beacon_point_ref import BeaconPointRef
from generated.border_point_ref import BorderPointRef
from generated.complex_feature_ref_structure import ComplexFeatureRefStructure
from generated.complex_feature_refs_rel_structure import (
    ComplexFeatureRefsRelStructure,
)
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.garage_point_ref import GaragePointRef
from generated.parking_point_ref import ParkingPointRef
from generated.point_ref import PointRef
from generated.projection_version_structure import ProjectionVersionStructure
from generated.railway_point_ref import RailwayPointRef
from generated.relief_point_ref import ReliefPointRef
from generated.road_point_ref import RoadPointRef
from generated.route_point_ref import RoutePointRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.timing_point_ref import TimingPointRef
from generated.traffic_control_point_ref import TrafficControlPointRef
from generated.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureProjectionVersionStructure(ProjectionVersionStructure):
    """
    Type for a COMPLEX FEATURE PROJECTION.

    :ivar projected_fearture_ref: COMPLEX FEATURE which is being
        projetced.
    :ivar onto_feature_ref: COMPLEX FEATURE onto which projection is
        being made.
    :ivar choice:
    :ivar features: COMPLEX FEATURES in PROJECTION.
    """

    class Meta:
        name = "ComplexFeatureProjection_VersionStructure"

    projected_fearture_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedFeartureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onto_feature_ref: Optional[ComplexFeatureRefStructure] = field(
        default=None,
        metadata={
            "name": "OntoFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: List[
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
        default_factory=list,
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
    features: Optional[ComplexFeatureRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
