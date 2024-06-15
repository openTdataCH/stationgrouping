from dataclasses import dataclass

from generated.path_assignment_ref_structure import PathAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathAssignmentRef(PathAssignmentRefStructure):
    """
    Reference to a PATH ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
