from dataclasses import dataclass

from generated.type_of_codespace_assignment_ref_structure import (
    TypeOfCodespaceAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCodespaceAssignmentRef(TypeOfCodespaceAssignmentRefStructure):
    """Reference to a TYPE OF CODESPACE ASSIGNMENT.

    +v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
