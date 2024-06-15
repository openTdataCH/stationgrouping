from dataclasses import dataclass

from generated.usage_parameter_price_versioned_child_structure import (
    UsageParameterPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameterPrice(UsageParameterPriceVersionedChildStructure):
    """A set of all possible price features of a FARE USAGE PARAMETER: default total price, discount in value or percentage etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
