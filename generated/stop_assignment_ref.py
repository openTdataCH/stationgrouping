from dataclasses import dataclass

from generated.stop_assignment_ref_structure import StopAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAssignmentRef(StopAssignmentRefStructure):
    """
    Reference to a STOP ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
