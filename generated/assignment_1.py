from dataclasses import dataclass

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Assignment1(AssignmentVersionStructure1):
    """A set of properties to be applied  to an another element.

    It has a name and an order.
    """

    class Meta:
        name = "Assignment"
        namespace = "http://www.netex.org.uk/netex"
