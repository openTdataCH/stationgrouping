from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.entity_in_version_structure import OperatingDay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDaysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of OPERATING DAY.
    """

    class Meta:
        name = "operatingDaysInFrame_RelStructure"

    operating_day: List[OperatingDay] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
