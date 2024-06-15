from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.country import Country

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CountriesInFrameRelStructure(ContainmentAggregationStructure):
    """Type for containment in frame of COUNTRies.

    +v1.1
    """

    class Meta:
        name = "countriesInFrame_RelStructure"

    country: List[Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
