from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.parking_bay_ref import ParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more a references to a PARKING BAY.
    """

    class Meta:
        name = "parkingBayRefs_RelStructure"

    parking_bay_ref: List[ParkingBayRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
