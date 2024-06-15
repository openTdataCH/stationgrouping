from dataclasses import dataclass

from generated.pricing_rule_ref_structure import PricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingRuleRef(PricingRuleRefStructure):
    """
    Reference to a PRICING RULE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
