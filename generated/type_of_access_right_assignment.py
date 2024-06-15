from dataclasses import dataclass

from generated.type_of_access_right_assignment_version_structure import (
    TypeOfAccessRightAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfAccessRightAssignment(TypeOfAccessRightAssignmentVersionStructure):
    """A classification of ACCESS RIGHT ASSIGNMENTs expressing their general
    functionalities and local functional characteristics specific to the operator.

    Types of ACCESS RIGHT ASSIGNMENTs like e.g. throw-away ticket,
    throw-away ticket unit, value card, electronic purse allowing
    access, public transport credit card etc. may be used to define
    these categories.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
