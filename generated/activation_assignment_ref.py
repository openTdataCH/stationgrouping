from dataclasses import dataclass

from generated.activation_assignment_ref_structure import (
    ActivationAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationAssignmentRef(ActivationAssignmentRefStructure):
    """
    Reference to an ACTIVATION ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
