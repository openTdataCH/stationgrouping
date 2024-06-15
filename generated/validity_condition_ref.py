from dataclasses import dataclass

from generated.validity_condition_ref_structure import (
    ValidityConditionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityConditionRef(ValidityConditionRefStructure):
    """
    Reference to a VALIDITY CONDITION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
