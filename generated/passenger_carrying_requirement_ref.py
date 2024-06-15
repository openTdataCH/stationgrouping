from dataclasses import dataclass

from generated.passenger_carrying_requirement_ref_structure import (
    PassengerCarryingRequirementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCarryingRequirementRef(
    PassengerCarryingRequirementRefStructure
):
    """
    Reference to a PASSENGER CARRYING REQUIREMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
