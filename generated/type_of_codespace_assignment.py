from dataclasses import dataclass

from generated.type_of_codespace_assignment_value_structure import (
    TypeOfCodespaceAssignmentValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCodespaceAssignment(TypeOfCodespaceAssignmentValueStructure):
    """
    Classification of an CODESPACE  ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
