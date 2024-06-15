from dataclasses import dataclass

from generated.dynamic_stop_assignment_version_structure import (
    DynamicStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicStopAssignment(DynamicStopAssignmentVersionStructure):
    """
    Change to a PASSENGER STOP ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
