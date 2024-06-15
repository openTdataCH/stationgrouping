from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.topographic_place_ref_structure import (
    TopographicPlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlaceRefsRelStructure(OneToManyRelationshipStructure):
    """
    A collection of one or more references to TOPOGRAPHIC PLACE.

    :ivar topographic_place_ref: Reference to the identifier of a
        TOPOGRAPHIC PLACE.
    """

    class Meta:
        name = "topographicPlaceRefs_RelStructure"

    topographic_place_ref: List[TopographicPlaceRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
