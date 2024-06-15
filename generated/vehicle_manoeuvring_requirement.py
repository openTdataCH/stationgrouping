from dataclasses import dataclass

from generated.vehicle_manoeuvring_requirement_version_structure import (
    VehicleManoeuvringRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleManoeuvringRequirement(
    VehicleManoeuvringRequirementVersionStructure
):
    """
    Requirements for carrying passengers.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
