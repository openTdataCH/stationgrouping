from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.path_link import PathLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of PATH LINKs.

    :ivar path_link: A designated path between two PLACEs. May include
        an Ordered sequence of references to PATH LINKS.
    """

    class Meta:
        name = "pathLinksInFrame_RelStructure"

    path_link: List[PathLink] = field(
        default_factory=list,
        metadata={
            "name": "PathLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
