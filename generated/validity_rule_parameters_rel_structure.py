from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.entity_in_version_structure import (
    ValidityRuleParameterVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityRuleParametersRelStructure(ContainmentAggregationStructure):
    """
    A collection of one or more VALIDITY PARAMETERs.

    :ivar validity_rule_parameter: Parameter for a rule of a user
        defined VALIDITY CONDITION used by a rule for selecting
        versions. E.g. river level &gt; 1,5 m and bad weather.
    """

    class Meta:
        name = "validityRuleParameters_RelStructure"

    validity_rule_parameter: List[ValidityRuleParameterVersionStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "ValidityRuleParameter",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
