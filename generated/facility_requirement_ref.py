from dataclasses import dataclass

from generated.facility_requirement_ref_structure import (
    FacilityRequirementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRequirementRef(FacilityRequirementRefStructure):
    """
    Reference to a FACILITY REQUIREMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
