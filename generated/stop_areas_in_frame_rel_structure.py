from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.stop_area import StopArea

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAreasInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of STOP AREAs.
    """

    class Meta:
        name = "stopAreasInFrame_RelStructure"

    stop_area: List[StopArea] = field(
        default_factory=list,
        metadata={
            "name": "StopArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
