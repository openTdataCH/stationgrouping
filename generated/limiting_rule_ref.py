from dataclasses import dataclass

from generated.limiting_rule_ref_structure import LimitingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LimitingRuleRef(LimitingRuleRefStructure):
    """
    Reference to a LIMITING RULE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
