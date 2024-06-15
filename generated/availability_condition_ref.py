from dataclasses import dataclass

from generated.availability_condition_ref_structure import (
    AvailabilityConditionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AvailabilityConditionRef(AvailabilityConditionRefStructure):
    """Reference to an AVAILABILITY CONDITION.

    A VALIDITY CONDITION defined in terms of temporal attributes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
