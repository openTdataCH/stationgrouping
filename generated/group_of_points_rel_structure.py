from dataclasses import dataclass, field
from typing import List

from generated.group_of_points import GroupOfPoints
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPointsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of GROUPs OF POINTs.
    """

    class Meta:
        name = "groupOfPoints_RelStructure"

    group_of_points: List[GroupOfPoints] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
