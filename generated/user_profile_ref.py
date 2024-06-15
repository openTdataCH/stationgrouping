from dataclasses import dataclass

from generated.user_profile_ref_structure import UserProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileRef(UserProfileRefStructure):
    """
    Reference to a USER PROFILE usage parameter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
