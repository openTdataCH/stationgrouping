from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.data_source import DataSource

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSourcesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DATA SOURCE.
    """

    class Meta:
        name = "dataSourcesInFrame_RelStructure"

    data_source: List[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
