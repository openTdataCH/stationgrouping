from dataclasses import dataclass, field
from typing import Any

from generated.limiting_rule_versioned_structure import (
    LimitingRuleVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LimitingRuleInContext(LimitingRuleVersionedStructure):
    """OPTIMISED version whcih can be be used only in line assues ID of comtainign
    context  -no  id checking.

    A price for which a discount can be offered.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
