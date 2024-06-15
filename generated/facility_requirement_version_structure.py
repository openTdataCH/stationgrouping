from dataclasses import dataclass, field
from typing import Optional

from generated.service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from generated.vehicle_requirement_version_structure import (
    VehicleRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRequirementVersionStructure(VehicleRequirementVersionStructure):
    """
    Type for a FACILITY REQUIREMENT.

    :ivar facility_sets: Facilities required for VEHICLE.
    """

    class Meta:
        name = "FacilityRequirement_VersionStructure"

    facility_sets: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "facilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
