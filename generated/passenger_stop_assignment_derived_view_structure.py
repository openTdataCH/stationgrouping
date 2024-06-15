from dataclasses import dataclass, field
from typing import Optional, Union

from generated.derived_view_structure import DerivedViewStructure
from generated.dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from generated.multilingual_string import MultilingualString
from generated.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from generated.quay_ref_structure import QuayRefStructure
from generated.stop_place_ref import StopPlaceRef
from generated.vehicle_journey_stop_assignment_ref import (
    VehicleJourneyStopAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignmentDerivedViewStructure(DerivedViewStructure):
    """
    Type for a PASSENGER STOP POINT ASSIGNMENT VIEW.

    :ivar
        vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref:
    :ivar stop_place_ref:
    :ivar quay_ref: QUAY to which SCHEDULED STOP POINT is to be
        assigned.
    :ivar quay_name: Name of QUAY or platform to which the SCHEDULED
        STOP POINT is assigned.
    :ivar label:
    :ivar order: Order of Assignment.
    """

    class Meta:
        name = "PassengerStopAssignment_DerivedViewStructure"

    vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref: Optional[
        Union[
            VehicleJourneyStopAssignmentRef,
            DynamicStopAssignmentRef,
            PassengerStopAssignmentRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_ref: Optional[QuayRefStructure] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "QuayName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
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
