from dataclasses import dataclass, field
from typing import Optional, Union

from generated.boarding_position import BoardingPosition
from generated.boarding_position_ref import BoardingPositionRef
from generated.quay import Quay
from generated.quay_ref import QuayRef
from generated.stop_assignment_version_structure import (
    StopAssignmentVersionStructure,
)
from generated.stop_place import StopPlace
from generated.stop_place_ref import StopPlaceRef
from generated.train_stop_assignments_rel_structure import (
    TrainStopAssignmentsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    """
    Type for a PASSENGER STOP ASSIGNMENT.

    :ivar stop_place_ref_or_stop_place:
    :ivar quay_ref_or_quay:
    :ivar boarding_position_ref_or_boarding_position:
    :ivar train_elements: Train elements to which SCHEDULED STOP POINT
        is to be assigned.
    """

    class Meta:
        name = "PassengerStopAssignment_VersionStructure"

    stop_place_ref_or_stop_place: Optional[Union[StopPlaceRef, StopPlace]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "StopPlaceRef",
                        "type": StopPlaceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "StopPlace",
                        "type": StopPlace,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    quay_ref_or_quay: Optional[Union[QuayRef, Quay]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    boarding_position_ref_or_boarding_position: Optional[
        Union[BoardingPositionRef, BoardingPosition]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_elements: Optional[TrainStopAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "trainElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
