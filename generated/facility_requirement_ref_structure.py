from dataclasses import dataclass

from generated.vehicle_requirement_ref_structure import (
    VehicleRequirementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRequirementRefStructure(VehicleRequirementRefStructure):
    """
    Type for a reference to a FACILITY REQUIRMENT.
    """
