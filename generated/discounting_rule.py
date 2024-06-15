from dataclasses import dataclass

from generated.discounting_rule_versioned_structure import (
    DiscountingRuleVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DiscountingRule(DiscountingRuleVersionedStructure):
    """
    A price for which a discount can be offered.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
