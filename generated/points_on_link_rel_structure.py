from dataclasses import dataclass, field
from typing import List, Optional

from generated.line_string_type import LineStringType
from generated.point_on_link import PointOnLink
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointsOnLinkRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of POINTs ON LINK.
    """

    class Meta:
        name = "pointsOnLink_RelStructure"

    point_on_link: List[PointOnLink] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
    line_string: Optional[LineStringType] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
