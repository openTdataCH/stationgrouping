from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfAccessRightAssignmentVersionStructure(
    TypeOfEntityVersionStructure
):
    """
    Type for TYPE OF ACCESS RIGHT ASSIGNMENT.
    """

    class Meta:
        name = "TypeOfAccessRightAssignment_VersionStructure"
