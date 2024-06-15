from dataclasses import dataclass

from generated.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRightParameterAssignmentRefStructure(AssignmentRefStructure):
    """
    Type for Reference to an ACCESS RIGHT PARAMETER ASSIGNMENT.
    """
