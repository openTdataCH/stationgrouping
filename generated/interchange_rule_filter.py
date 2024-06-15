from dataclasses import dataclass

from generated.interchange_rule_parameter_structure import (
    InterchangeRuleParameterStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleFilter(InterchangeRuleParameterStructure):
    """
    Filter for  INTERCHANGE RULE Filter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
