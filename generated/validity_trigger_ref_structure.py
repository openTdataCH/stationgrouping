from dataclasses import dataclass

from generated.validity_condition_ref_structure import (
    ValidityConditionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityTriggerRefStructure(ValidityConditionRefStructure):
    """
    Type for a reference to a VALIDITY TRIGGER.
    """
