from dataclasses import dataclass, field
from typing import Optional, Union

from generated.railway_link_ref import RailwayLinkRef
from generated.railway_point_ref import RailwayPointRef
from generated.road_link_ref import RoadLinkRef
from generated.road_point_ref import RoadPointRef
from generated.stop_place_space_version_structure import (
    StopPlaceSpaceVersionStructure,
)
from generated.vehicle_quay_alignments_rel_structure import (
    VehicleQuayAlignmentsRelStructure,
)
from generated.vehicle_stopping_positions_rel_structure import (
    VehicleStoppingPositionsRelStructure,
)
from generated.wire_link_ref import WireLinkRef
from generated.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlaceVersionStructure(StopPlaceSpaceVersionStructure):
    """
    Type for a VEHICLE STOPPING PLACE.

    :ivar wire_link_ref_or_road_link_ref_or_railway_link_ref:
    :ivar wire_point_ref_or_road_point_ref_or_railway_point_ref:
    :ivar vehicle_stopping_positions: Designated Positions within a
        VEHICLE STOPPING PLACE for a VEHICLE to stop.
    :ivar quay_alignments: QUAYs with which the VEHICLE STOPPING PLACE
        aligns.
    """

    class Meta:
        name = "VehicleStoppingPlace_VersionStructure"

    wire_link_ref_or_road_link_ref_or_railway_link_ref: Optional[
        Union[WireLinkRef, RoadLinkRef, RailwayLinkRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    wire_point_ref_or_road_point_ref_or_railway_point_ref: Optional[
        Union[WirePointRef, RoadPointRef, RailwayPointRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    vehicle_stopping_positions: Optional[
        VehicleStoppingPositionsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleStoppingPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_alignments: Optional[VehicleQuayAlignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "quayAlignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
