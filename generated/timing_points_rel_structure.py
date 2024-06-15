from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.timing_point import TimingPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPointsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TIMING POINTs.

    :ivar timing_point: TIMING POINT.
    """

    class Meta:
        name = "timingPoints_RelStructure"

    timing_point: List[TimingPoint] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
