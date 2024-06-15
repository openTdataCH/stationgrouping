from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.stop_place import StopPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of STOP PLACE.
    """

    class Meta:
        name = "stopPlacesInFrame_RelStructure"

    stop_place: List[StopPlace] = field(
        default_factory=list,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
