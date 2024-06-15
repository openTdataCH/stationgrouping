from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.type_of_point_ref import TypeOfPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPointRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF POINT.
    """

    class Meta:
        name = "typeOfPointRefs_RelStructure"

    type_of_point_ref: List[TypeOfPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
