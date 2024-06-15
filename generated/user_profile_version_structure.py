from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlPeriod

from generated.companion_profiles_rel_structure import (
    CompanionProfilesRelStructure,
)
from generated.discount_basis_enumeration import DiscountBasisEnumeration
from generated.gender_limitation import GenderLimitation
from generated.proof_of_identity_enumeration import ProofOfIdentityEnumeration
from generated.residential_qualifications_rel_structure import (
    ResidentialQualificationsRelStructure,
)
from generated.type_of_concession_ref import TypeOfConcessionRef
from generated.usage_parameter_version_structure import (
    UsageParameterVersionStructure,
)
from generated.user_profile_ref_structure import UserProfileRefStructure
from generated.user_type_enumeration import UserTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileVersionStructure(UsageParameterVersionStructure):
    """
    Type for USER PROFILE.

    :ivar base_user_profile_ref: Base Profile on which this User profile
        is based. Assume all properties from base that are not
        explicitly stated on subprofile.
    :ivar type_of_concession_ref:
    :ivar user_type: Classification of user profile.
    :ivar minimum_age: Minimum age to be eligible for profile.
    :ivar maximum_age: Maximum age to be eligible for profile.
    :ivar month_day_on_which_age_applies: Date on which Age Applies, if
        fixed annually.
    :ivar minimum_height: Minimum height to be eligible for profile.
    :ivar maximum_height: Maximum height to be eligible for profile.
    :ivar local_resident: Whether user must be Local Resident.
    :ivar resides: Minimum and maximum numbers of users in each category
        allowed on GROUP TICKET.
    :ivar gender_limitation:
    :ivar proof_required: Type of document accepted as proof of
        eligibility.
    :ivar discount_basis: Nature of discount for this profile.
    :ivar companion_profiles: Minimum and maximum numbers of users in
        each category  allowed on GROUP TICKET.
    """

    class Meta:
        name = "UserProfile_VersionStructure"

    base_user_profile_ref: Optional[UserProfileRefStructure] = field(
        default=None,
        metadata={
            "name": "BaseUserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_concession_ref: Optional[TypeOfConcessionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_type: Optional[UserTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "UserType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    month_day_on_which_age_applies: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "MonthDayOnWhichAgeApplies",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    local_resident: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LocalResident",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    resides: Optional[ResidentialQualificationsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender_limitation: Optional[GenderLimitation] = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    proof_required: List[ProofOfIdentityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ProofRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    discount_basis: Optional[DiscountBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "DiscountBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    companion_profiles: Optional[CompanionProfilesRelStructure] = field(
        default=None,
        metadata={
            "name": "companionProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
