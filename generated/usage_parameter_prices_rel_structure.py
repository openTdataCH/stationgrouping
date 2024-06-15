from dataclasses import dataclass, field
from typing import List, Union

from generated.cell_ref import CellRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.usage_parameter_price import UsageParameterPrice
from generated.usage_parameter_price_ref import UsageParameterPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameterPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE USAGE PARAMETER PRICEs.
    """

    class Meta:
        name = "usageParameterPrices_RelStructure"

    usage_parameter_price_ref_or_usage_parameter_price_or_cell_ref: List[
        Union[UsageParameterPriceRef, UsageParameterPrice, CellRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
