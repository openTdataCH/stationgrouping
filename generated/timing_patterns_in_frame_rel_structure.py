from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.timing_pattern import TimingPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPatternsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TIMING PATTERN.
    """

    class Meta:
        name = "timingPatternsInFrame_RelStructure"

    timing_pattern: List[TimingPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
