from dataclasses import dataclass

from generated.train_component_label_assignment_version_structure import (
    TrainComponentLabelAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentLabelAssignment(
    TrainComponentLabelAssignmentVersionStructure
):
    """
    The allocation of an advertised designation for a vehicle or vehicle element
    for passengers.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
