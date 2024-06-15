from dataclasses import dataclass

from generated.pricing_rule_versioned_structure import (
    PricingRuleVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingRule(PricingRuleVersionedStructure):
    """
    Parameters describing how a fare is to be computed.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
