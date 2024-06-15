from dataclasses import dataclass, field
from typing import List, Union

from generated.companion_profile import CompanionProfile
from generated.companion_profile_ref import CompanionProfileRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompanionProfilesRelStructure(OneToManyRelationshipStructure):
    """
    Type for  a list of COMPANION PROFILEs.
    """

    class Meta:
        name = "companionProfiles_RelStructure"

    companion_profile_ref_or_companion_profile: List[
        Union[CompanionProfileRef, CompanionProfile]
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
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
