from dataclasses import dataclass, field
from typing import List

from generated.garage_ref import GarageRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GarageRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a GARAGE.
    """

    class Meta:
        name = "garageRefs_RelStructure"

    garage_ref: List[GarageRef] = field(
        default_factory=list,
        metadata={
            "name": "GarageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
