from dataclasses import dataclass

from generated.pricing_rule_ref_structure import PricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DiscountingRuleRefStructure(PricingRuleRefStructure):
    """
    Type for Reference to a DISCOUNTING RULE.
    """
