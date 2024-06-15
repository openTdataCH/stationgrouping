from dataclasses import dataclass

from generated.discounting_rule_ref_structure import (
    DiscountingRuleRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LimitingRuleRefStructure(DiscountingRuleRefStructure):
    """
    Type for Reference to a LIMITING RULE.
    """
