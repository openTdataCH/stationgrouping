from dataclasses import dataclass

from generated.access_right_parameter_assignment_version_structure import (
    AccessRightParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRightParameterAssignment(
    AccessRightParameterAssignmentVersionStructure
):
    """
    The assignment of a fare parameter (referring to geography, time, quality or
    usage) to an element of a fare system (access right, validated access, control
    mean, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
