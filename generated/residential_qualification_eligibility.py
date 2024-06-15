from dataclasses import dataclass

from generated.residential_qualification_eligibility_versioned_child_structure import (
    ResidentialQualificationEligibilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationEligibility(
    ResidentialQualificationEligibilityVersionedChildStructure
):
    """
    Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a
    specific RESIDENTIAL QUALIFICATION as a validity parameter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
