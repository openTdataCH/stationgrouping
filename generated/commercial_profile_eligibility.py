from dataclasses import dataclass

from generated.commercial_profile_eligibility_versioned_child_structure import (
    CommercialProfileEligibilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommercialProfileEligibility(
    CommercialProfileEligibilityVersionedChildStructure
):
    """
    Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a
    specific COMMERCIAL PROFILE as a validity parameter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
