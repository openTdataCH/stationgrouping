from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCodespaceAssignmentValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF CODESPACE ASSIGNMENT.
    """

    class Meta:
        name = "TypeOfCodespaceAssignment_ValueStructure"
