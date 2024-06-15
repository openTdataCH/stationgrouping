from dataclasses import dataclass, field
from typing import Optional, Union

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.dead_run_ref import DeadRunRef
from generated.multilingual_string import MultilingualString
from generated.train_component_ref import TrainComponentRef
from generated.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentLabelAssignmentVersionStructure(
    AssignmentVersionStructure1
):
    """
    Type for TRAIN COMPONENT NUMBER ASSIGNNMENT.

    :ivar label: Label to assign.
    :ivar dead_run_ref_or_vehicle_journey_ref:
    :ivar train_component_ref:
    """

    class Meta:
        name = "TrainComponentLabelAssignment_VersionStructure"

    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
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
    train_component_ref: TrainComponentRef = field(
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
