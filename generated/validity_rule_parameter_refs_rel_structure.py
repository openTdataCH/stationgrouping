from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.validity_rule_parameter_ref import ValidityRuleParameterRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityRuleParameterRefsRelStructure(OneToManyRelationshipStructure):
    """
    A collection of one or more VALIDITY RULE PARAMETERs.
    """

    class Meta:
        name = "validityRuleParameterRefs_RelStructure"

    validity_rule_parameter_ref: List[ValidityRuleParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityRuleParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
