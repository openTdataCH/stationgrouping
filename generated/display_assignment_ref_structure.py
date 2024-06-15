from dataclasses import dataclass, field

from generated.assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DisplayAssignmentRefStructure(AssignmentRefStructure):
    """
    Type for a reference to a DISPLAY ASSIGNMENT.

    :ivar order: Relative oOrder of ASSIGNMENT.
    """

    order: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
