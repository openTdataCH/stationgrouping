from dataclasses import dataclass

from generated.type_of_responsibility_role_value_structure import (
    TypeOfResponsibilityRoleValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfResponsibilityRole(TypeOfResponsibilityRoleValueStructure):
    """
    Classification of a RESPONSIBILITY ROLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
