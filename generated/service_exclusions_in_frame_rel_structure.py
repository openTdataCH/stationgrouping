from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.service_exclusion import ServiceExclusion

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceExclusionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SERVICE EXCLUSION.
    """

    class Meta:
        name = "serviceExclusionsInFrame_RelStructure"

    service_exclusion: List[ServiceExclusion] = field(
        default_factory=list,
        metadata={
            "name": "ServiceExclusion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
