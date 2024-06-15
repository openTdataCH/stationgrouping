from dataclasses import dataclass

from generated.limiting_rule_versioned_structure import (
    LimitingRuleVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LimitingRule(LimitingRuleVersionedStructure):
    """
    A price for which a discount can be offered.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
