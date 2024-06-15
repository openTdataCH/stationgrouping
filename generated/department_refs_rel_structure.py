from dataclasses import dataclass, field
from typing import List

from generated.department_ref import DepartmentRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DepartmentRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of DEPARTMENTs.
    """

    class Meta:
        name = "departmentRefs_RelStructure"

    department_ref: List[DepartmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
