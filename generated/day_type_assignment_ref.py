from dataclasses import dataclass

from generated.day_type_assignment_ref_structure import (
    DayTypeAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypeAssignmentRef(DayTypeAssignmentRefStructure):
    """
    Reference to a DAY TYPE ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
