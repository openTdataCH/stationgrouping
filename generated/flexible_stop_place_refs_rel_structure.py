from dataclasses import dataclass, field
from typing import List

from generated.flexible_stop_place_ref import FlexibleStopPlaceRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopPlaceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a FLEXIBLE STOP PLACE.
    """

    class Meta:
        name = "flexibleStopPlaceRefs_RelStructure"

    flexible_stop_place_ref: List[FlexibleStopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
