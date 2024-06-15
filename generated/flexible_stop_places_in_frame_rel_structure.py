from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.flexible_stop_place import FlexibleStopPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of FLEXIBLE STOP PLACE.
    """

    class Meta:
        name = "flexibleStopPlacesInFrame_RelStructure"

    flexible_stop_place: List[FlexibleStopPlace] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleStopPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
