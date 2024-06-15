from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.topographic_place import TopographicPlace
from generated.topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlacesRelStructure(ContainmentAggregationStructure):
    """
    Collection of TOPOGRAPHIC PLACEs.
    """

    class Meta:
        name = "topographicPlaces_RelStructure"

    topographic_place_ref: List[TopographicPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
