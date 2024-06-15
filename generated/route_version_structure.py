from dataclasses import dataclass, field
from typing import Optional, Union

from generated.direction_ref import DirectionRef
from generated.direction_type import DirectionType
from generated.flexible_line_ref import FlexibleLineRef
from generated.line_ref import LineRef
from generated.points_on_route_rel_structure import PointsOnRouteRelStructure
from generated.route_ref_structure import RouteRefStructure
from generated.sections_in_sequence_rel_structure import (
    LinkSequenceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteVersionStructure(LinkSequenceVersionStructure):
    """
    Type for ROUTE.

    :ivar flexible_line_ref_or_line_ref:
    :ivar direction_type:
    :ivar direction_ref:
    :ivar points_in_sequence: Ordered set of points making up a ROUTE.
    :ivar inverse_route_ref: Reference to the corresponding matching
        ROUTE in the  oppositte direction, if any.
    """

    class Meta:
        name = "Route_VersionStructure"

    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
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
            ),
        },
    )
    direction_type: Optional[DirectionType] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_sequence: Optional[PointsOnRouteRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    inverse_route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "InverseRouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
