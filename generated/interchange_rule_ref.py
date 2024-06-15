from dataclasses import dataclass

from generated.interchange_rule_ref_structure import (
    InterchangeRuleRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleRef(InterchangeRuleRefStructure):
    """
    Reference to an INTERCHANGE RULE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
