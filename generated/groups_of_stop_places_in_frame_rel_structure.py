from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.group_of_stop_places import GroupOfStopPlaces

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfStopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GROUP OF STOP PLACEs.
    """

    class Meta:
        name = "groupsOfStopPlacesInFrame_RelStructure"

    group_of_stop_places: List[GroupOfStopPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfStopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
