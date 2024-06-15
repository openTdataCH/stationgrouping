from dataclasses import dataclass

from generated.vehicle_requirement_version_structure import (
    VehicleRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRequirement(VehicleRequirementVersionStructure):
    """
    Requirements for service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
