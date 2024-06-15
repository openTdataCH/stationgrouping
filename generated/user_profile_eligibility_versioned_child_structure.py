from dataclasses import dataclass, field
from typing import Optional, Union

from generated.companion_profile_ref import CompanionProfileRef
from generated.customer_eligibility_versioned_child_structure import (
    CustomerEligibilityVersionedChildStructure,
)
from generated.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileEligibilityVersionedChildStructure(
    CustomerEligibilityVersionedChildStructure
):
    """
    Type for USER PROFILE ELIGIBILITY.
    """

    class Meta:
        name = "UserProfileEligibility_VersionedChildStructure"

    companion_profile_ref_or_user_profile_ref: Optional[
        Union[CompanionProfileRef, UserProfileRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
