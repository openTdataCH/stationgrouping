from dataclasses import dataclass, field
from typing import Optional, Union

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.compound_train_ref import CompoundTrainRef
from generated.dead_run_ref import DeadRunRef
from generated.train_ref import TrainRef
from generated.vehicle_journey_ref import VehicleJourneyRef
from generated.vehicle_orientation_enumeration import (
    VehicleOrientationEnumeration,
)
from generated.vehicle_stopping_position_ref import VehicleStoppingPositionRef
from generated.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeStopAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for VEHICLE TYPE STOP ASSIGNNMENT.

    :ivar vehicle_orientation: Relative orientation of vehicle - Default
        is forwards.
    :ivar vehicle_stopping_position_ref:
    :ivar dead_run_ref_or_vehicle_journey_ref:
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    """

    class Meta:
        name = "VehicleTypeStopAssignment_VersionStructure"

    vehicle_orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_stopping_position_ref: Optional[VehicleStoppingPositionRef] = (
        field(
            default=None,
            metadata={
                "name": "VehicleStoppingPositionRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    dead_run_ref_or_vehicle_journey_ref: Optional[
        Union[DeadRunRef, VehicleJourneyRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
