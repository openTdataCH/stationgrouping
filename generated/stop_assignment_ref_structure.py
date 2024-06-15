from dataclasses import dataclass

from generated.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAssignmentRefStructure(AssignmentRefStructure):
    """
    Type for a reference to a STOP ASSIGNMENT.
    """
