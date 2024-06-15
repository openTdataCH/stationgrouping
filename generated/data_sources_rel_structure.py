from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.data_source import DataSource
from generated.data_source_ref import DataSourceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSourcesRelStructure(ContainmentAggregationStructure):
    """
    Type for list of DATA SOURCEs.
    """

    class Meta:
        name = "dataSources_RelStructure"

    data_source_ref_or_data_source: List[Union[DataSourceRef, DataSource]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "DataSourceRef",
                        "type": DataSourceRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "DataSource",
                        "type": DataSource,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
