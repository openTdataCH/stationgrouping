from dataclasses import dataclass, field
from typing import Optional

from generated.priceable_object_version_structure import (
    PriceableObjectVersionStructure,
)
from generated.type_of_usage_parameter_ref import TypeOfUsageParameterRef
from generated.usage_parameter_prices_rel_structure import (
    UsageParameterPricesRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameterVersionStructure(PriceableObjectVersionStructure):
    """
    Type for USAGE PARAMETER.

    :ivar type_of_usage_parameter_ref:
    :ivar prices: Prices associated with USAGE PARAMETER.
    """

    class Meta:
        name = "UsageParameter_VersionStructure"

    type_of_usage_parameter_ref: Optional[TypeOfUsageParameterRef] = field(
        default=None,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[UsageParameterPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
