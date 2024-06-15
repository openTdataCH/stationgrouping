from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.topographic_place import TopographicPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlacesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TOPOGRAPHIC PLACEs.
    """

    class Meta:
        name = "topographicPlacesInFrame_RelStructure"

    topographic_place: List[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
