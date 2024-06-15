from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.version import Version

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VERSION.
    """

    class Meta:
        name = "versionsInFrame_RelStructure"

    version: List[Version] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
