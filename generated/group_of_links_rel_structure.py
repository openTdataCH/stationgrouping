from dataclasses import dataclass, field
from typing import List

from generated.group_of_links import GroupOfLinks
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinksRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of GROUPs OF LINKs.
    """

    class Meta:
        name = "groupOfLinks_RelStructure"

    group_of_links: List[GroupOfLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
