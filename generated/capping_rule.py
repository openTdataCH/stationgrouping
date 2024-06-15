from dataclasses import dataclass

from generated.capping_rule_versioned_child_structure import (
    CappingRuleVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappingRule(CappingRuleVersionedChildStructure):
    """
    Rule about capping for a mode.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
