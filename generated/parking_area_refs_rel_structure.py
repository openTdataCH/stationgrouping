from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.parking_area_ref import ParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingAreaRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a PARKING AREA.
    """

    class Meta:
        name = "parkingAreaRefs_RelStructure"

    parking_area_ref: List[ParkingAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
