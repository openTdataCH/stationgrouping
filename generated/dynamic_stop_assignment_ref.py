from dataclasses import dataclass

from generated.dynamic_stop_assignment_ref_structure import (
    DynamicStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicStopAssignmentRef(DynamicStopAssignmentRefStructure):
    """
    Reference to a DYNAMIC STOP ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
