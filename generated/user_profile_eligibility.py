from dataclasses import dataclass

from generated.user_profile_eligibility_versioned_child_structure import (
    UserProfileEligibilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileEligibility(UserProfileEligibilityVersionedChildStructure):
    """
    Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a
    specific USER PROFILE as a validity parameter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
