from dataclasses import dataclass

from generated.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssignmentRef(AssignmentRefStructure):
    """
    Reference to a ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
