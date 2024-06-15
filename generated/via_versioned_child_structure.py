from dataclasses import dataclass, field
from typing import Optional, Union

from generated.border_point_ref import BorderPointRef
from generated.destination_display_ref import DestinationDisplayRef
from generated.destination_display_view import DestinationDisplayView
from generated.entity_in_version_structure import VersionedChildStructure
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.garage_point_ref import GaragePointRef
from generated.multilingual_string import MultilingualString
from generated.parking_point_ref import ParkingPointRef
from generated.relief_point_ref import ReliefPointRef
from generated.route_point_ref import RoutePointRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.timing_point_ref import TimingPointRef
from generated.via_type_enumeration import ViaTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ViaVersionedChildStructure(VersionedChildStructure):
    """
    A secondary heading  (e.g. ROUTE POINT or other place) showing intermediate
    places on the way to a destination.

    :ivar destination_display_ref_or_destination_display_view_or_name:
    :ivar choice:
    :ivar via_type: Classification of meaning of via:
    """

    class Meta:
        name = "Via_VersionedChildStructure"

    destination_display_ref_or_destination_display_view_or_name: Optional[
        Union[
            DestinationDisplayRef, DestinationDisplayView, MultilingualString
        ]
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
                {
                    "name": "Name",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
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
            ),
        },
    )
    via_type: Optional[ViaTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ViaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
