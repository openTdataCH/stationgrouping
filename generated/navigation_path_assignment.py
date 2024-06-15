from dataclasses import dataclass

from generated.navigation_path_assignment_version_structure import (
    NavigationPathAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPathAssignment(NavigationPathAssignmentVersionStructure):
    """
    Assignment of a CONNECTION link to a NAVIGATION PATH.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
