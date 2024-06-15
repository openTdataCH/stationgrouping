from dataclasses import dataclass

from generated.type_of_pricing_rule_version_structure import (
    TypeOfPricingRuleVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPricingRule(TypeOfPricingRuleVersionStructure):
    """Classification of pricing rule.

    Can be used for VAT categories, etc.  +v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
