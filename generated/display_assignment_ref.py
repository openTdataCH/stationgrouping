from dataclasses import dataclass

from generated.display_assignment_ref_structure import (
    DisplayAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DisplayAssignmentRef(DisplayAssignmentRefStructure):
    """
    Reference to a DISPLAY ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
