from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.place_ref import PlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a PLACE.
    """

    class Meta:
        name = "placeRefs_RelStructure"

    place_ref: List[PlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
