from dataclasses import dataclass

from generated.responsibility_role_assignment_versioned_child_structure import (
    ResponsibilityRoleAssignmentVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilityRoleAssignment(
    ResponsibilityRoleAssignmentVersionedChildStructure
):
    """
    Assignment of a specific RESPONSIBILITY ROLE to a specific organisation and/or
    subdivision.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
