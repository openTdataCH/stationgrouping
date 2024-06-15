from dataclasses import dataclass

from generated.train_component_label_assignment_ref_structure import (
    TrainComponentLabelAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentLabelAssignmentRef(
    TrainComponentLabelAssignmentRefStructure
):
    """
    Reference to a TRAIN COMPONENT NUMBER ASSIGNNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
