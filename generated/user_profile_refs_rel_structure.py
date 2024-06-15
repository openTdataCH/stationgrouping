from dataclasses import dataclass, field
from typing import List, Union

from generated.companion_profile_ref import CompanionProfileRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of USAGE PROFILEs.
    """

    class Meta:
        name = "userProfileRefs_RelStructure"

    companion_profile_ref_or_user_profile_ref: List[
        Union[CompanionProfileRef, UserProfileRef]
    ] = field(
        default_factory=list,
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
