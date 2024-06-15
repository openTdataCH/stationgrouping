from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.flexible_area import FlexibleArea
from generated.flexible_area_ref import FlexibleAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleAreasRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FLEXIBLE AREAs.
    """

    class Meta:
        name = "flexibleAreas_RelStructure"

    flexible_area_ref_or_flexible_area: List[
        Union[FlexibleAreaRef, FlexibleArea]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleArea",
                    "type": FlexibleArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
