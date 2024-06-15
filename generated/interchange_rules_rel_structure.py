from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.interchange_rule import InterchangeRule
from generated.interchange_rule_ref import InterchangeRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRulesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of INTERCHANGE RULEs.
    """

    class Meta:
        name = "interchangeRules_RelStructure"

    interchange_rule_ref_or_interchange_rule: List[
        Union[InterchangeRuleRef, InterchangeRule]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InterchangeRuleRef",
                    "type": InterchangeRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRule",
                    "type": InterchangeRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
