from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.access_space_ref import AccessSpaceRef
from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.boarding_position_ref import BoardingPositionRef
from generated.multilingual_string import MultilingualString
from generated.operator_ref import OperatorRef
from generated.operator_view import OperatorView
from generated.parking_area_ref import ParkingAreaRef
from generated.parking_entrance_for_vehicles_ref import (
    ParkingEntranceForVehiclesRef,
)
from generated.parking_entrance_ref import ParkingEntranceRef
from generated.parking_passenger_entrance_ref import (
    ParkingPassengerEntranceRef,
)
from generated.parking_ref import ParkingRef
from generated.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from generated.point_of_interest_ref import PointOfInterestRef
from generated.point_of_interest_space_ref import PointOfInterestSpaceRef
from generated.quay_ref import QuayRef
from generated.scheduled_stop_point_ref_structure import (
    ScheduledStopPointRefStructure,
)
from generated.stop_area_ref_structure import StopAreaRefStructure
from generated.stop_place_entrance_ref import StopPlaceEntranceRef
from generated.stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteConnectionEndStructure:
    """
    Type for a SITE CONNECTION End.

    :ivar transport_mode: MODE of end point of TRANSFER . Default is all
        modes, i.e. all modes of referenced stop place and or stop
        point.
    :ivar stop_area_ref: Identifier of a Place at end point of transfer.
    :ivar scheduled_stop_point_ref: Identifier of end SCHEDULED STOP
        POINT of TRANSFER.
    :ivar choice:
    :ivar operator_ref_or_operator_view:
    :ivar label: Label at end of site connection.
    """

    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: List[
        Union[
            StopPlaceRef,
            AccessSpaceRef,
            BoardingPositionRef,
            QuayRef,
            StopPlaceEntranceRef,
            PointOfInterestRef,
            PointOfInterestSpaceRef,
            PointOfInterestEntranceRef,
            ParkingRef,
            ParkingAreaRef,
            ParkingEntranceForVehiclesRef,
            ParkingPassengerEntranceRef,
            ParkingEntranceRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntranceRef",
                    "type": StopPlaceEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": PointOfInterestSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntranceRef",
                    "type": PointOfInterestEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehiclesRef",
                    "type": ParkingEntranceForVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntranceRef",
                    "type": ParkingPassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceRef",
                    "type": ParkingEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    operator_ref_or_operator_view: Optional[
        Union[OperatorRef, OperatorView]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorView",
                    "type": OperatorView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
