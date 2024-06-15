from dataclasses import dataclass

from generated.vehicle_requirement_ref_structure import (
    VehicleRequirementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRequirementRef(VehicleRequirementRefStructure):
    """
    Reference to a VEHICLE REQUIREMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
