from dataclasses import dataclass, field
from typing import List

from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.timing_link import TimingLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinksRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of TIMING LINKs.
    """

    class Meta:
        name = "timingLinks_RelStructure"

    timing_link: List[TimingLink] = field(
        default_factory=list,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
