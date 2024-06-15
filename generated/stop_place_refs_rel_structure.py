from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a STOP PLACE.
    """

    class Meta:
        name = "stopPlaceRefs_RelStructure"

    stop_place_ref: List[StopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
