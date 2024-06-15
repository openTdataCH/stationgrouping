from dataclasses import dataclass, field
from typing import List

from generated.boarding_position_ref import BoardingPositionRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPositionRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a BOARDING POSITION.
    """

    class Meta:
        name = "boardingPositionRefs_RelStructure"

    boarding_position_ref: List[BoardingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
