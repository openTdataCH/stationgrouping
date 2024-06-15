from dataclasses import dataclass

from generated.validity_condition_ref_structure import (
    ValidityConditionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AvailabilityConditionRefStructure(ValidityConditionRefStructure):
    """
    Type for a reference to an AVAILABILITY CONDITION.
    """
