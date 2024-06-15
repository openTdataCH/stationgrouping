from dataclasses import dataclass

from generated.user_profile_eligibility_ref_structure import (
    UserProfileEligibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileEligibilityRef(UserProfileEligibilityRefStructure):
    """
    Reference to a USER PROFILE ELIGIBILITY..
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
