from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.flexible_point_properties import FlexiblePointProperties

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexiblePointPropertiesRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of FLEXIBLE POINT PROPERTies.
    """

    class Meta:
        name = "flexiblePointProperties_RelStructure"

    flexible_point_properties: List[FlexiblePointProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
