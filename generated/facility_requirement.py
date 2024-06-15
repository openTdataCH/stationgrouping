from dataclasses import dataclass

from generated.facility_requirement_version_structure import (
    FacilityRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRequirement(FacilityRequirementVersionStructure):
    """
    Requirements for carrying passengers.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
