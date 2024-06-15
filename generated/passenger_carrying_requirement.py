from dataclasses import dataclass

from generated.passenger_carrying_requirement_version_structure import (
    PassengerCarryingRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCarryingRequirement(
    PassengerCarryingRequirementVersionStructure
):
    """
    Requirements for carrying passengers on a service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
