from dataclasses import dataclass, field
from typing import Optional, Union

from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.derived_view_structure import DerivedViewStructure
from generated.direction_view import DirectionView
from generated.flexible_line_ref import FlexibleLineRef
from generated.line_ref import LineRef
from generated.line_view import LineView
from generated.link_sequence_projection_ref import LinkSequenceProjectionRef
from generated.multilingual_string import MultilingualString
from generated.route_ref import RouteRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteDerivedViewStructure(DerivedViewStructure):
    """
    Type for ROUTE VIEW.

    :ivar route_ref:
    :ivar vehicle_mode: Mode of ROUTE.
    :ivar name: Name of Link Sequence.
    :ivar flexible_line_ref_or_line_ref_or_line_view:
    :ivar direction_view:
    :ivar link_sequence_projection_ref:
    """

    class Meta:
        name = "Route_DerivedViewStructure"

    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_line_ref_or_line_ref_or_line_view: Optional[
        Union[FlexibleLineRef, LineRef, LineView]
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
                    "name": "LineView",
                    "type": LineView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_view: Optional[DirectionView] = field(
        default=None,
        metadata={
            "name": "DirectionView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    link_sequence_projection_ref: Optional[LinkSequenceProjectionRef] = field(
        default=None,
        metadata={
            "name": "LinkSequenceProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
