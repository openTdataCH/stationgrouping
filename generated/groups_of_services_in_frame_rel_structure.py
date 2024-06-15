from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.group_of_services import GroupOfServices

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfServicesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GROUP OF SERVICEs.
    """

    class Meta:
        name = "groupsOfServicesInFrame_RelStructure"

    group_of_services: List[GroupOfServices] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
