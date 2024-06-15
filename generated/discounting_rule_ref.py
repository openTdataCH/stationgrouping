from dataclasses import dataclass

from generated.discounting_rule_ref_structure import (
    DiscountingRuleRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DiscountingRuleRef(DiscountingRuleRefStructure):
    """
    Reference to a DISCOUNTING RULE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
