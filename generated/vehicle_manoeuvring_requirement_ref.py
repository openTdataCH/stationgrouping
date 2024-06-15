from dataclasses import dataclass

from generated.vehicle_manoeuvring_requirement_ref_structure import (
    VehicleManoeuvringRequirementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleManoeuvringRequirementRef(
    VehicleManoeuvringRequirementRefStructure
):
    """
    Reference to a VEHICLE MANOEUVRING REQUIREMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
