from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.day_type_assignment import DayTypeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypeAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DAY TYPE ASSIGNMENTs.
    """

    class Meta:
        name = "dayTypeAssignmentsInFrame_RelStructure"

    day_type_assignment: List[DayTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
