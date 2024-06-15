from dataclasses import dataclass, field
from typing import List, Union

from generated.point_on_line_section import PointOnLineSection
from generated.point_on_section import PointOnSection
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointsOnSectionRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of  POINTS on SECTION POINT   +v1.1.
    """

    class Meta:
        name = "pointsOnSection_RelStructure"

    point_on_line_section_or_point_on_section: List[
        Union[PointOnLineSection, PointOnSection]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOnLineSection",
                    "type": PointOnLineSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOnSection",
                    "type": PointOnSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
