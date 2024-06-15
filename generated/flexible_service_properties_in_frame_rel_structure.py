from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.flexible_service_properties import FlexibleServiceProperties

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleServicePropertiesInFrameRelStructure(
    ContainmentAggregationStructure
):
    """
    Type for containment in frame of  FLEXIBLE SERVICE PROPERTies.
    """

    class Meta:
        name = "flexibleServicePropertiesInFrame_RelStructure"

    flexible_service_properties: List[FlexibleServiceProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
