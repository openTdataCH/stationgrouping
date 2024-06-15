from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.duty import Duty

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DutiesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DUTies.
    """

    class Meta:
        name = "dutiesInFrame_RelStructure"

    duty: List[Duty] = field(
        default_factory=list,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
