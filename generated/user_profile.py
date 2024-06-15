from dataclasses import dataclass

from generated.user_profile_version_structure import (
    UserProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfile(UserProfileVersionStructure):
    """
    The social profile of a passenger, based on age group, education, profession,
    social status, sex etc., often used for allowing discounts: 18-40 years old,
    graduates, drivers, unemployed, women etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
