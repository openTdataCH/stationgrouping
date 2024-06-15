from dataclasses import dataclass

from generated.type_of_access_right_assignment_ref_structure import (
    TypeOfAccessRightAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfAccessRightAssignmentRef(TypeOfAccessRightAssignmentRefStructure):
    """
    Reference to a TYPE OF ACCESS RIGHT ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
