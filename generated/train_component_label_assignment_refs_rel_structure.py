from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.train_component_label_assignment_ref import (
    TrainComponentLabelAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentLabelAssignmentRefsRelStructure(
    OneToManyRelationshipStructure
):
    """
    Type for a list of TRAIN COMPONENT NUMBER ASSIGNNMENTs.
    """

    class Meta:
        name = "TrainComponentLabelAssignmentRefs_RelStructure"

    train_component_label_assignment_ref: List[
        TrainComponentLabelAssignmentRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
