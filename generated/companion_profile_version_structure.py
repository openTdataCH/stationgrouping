from dataclasses import dataclass, field
from typing import Optional, Union

from generated.companion_profile_ref import CompanionProfileRef
from generated.companion_relationship_enumeration import (
    CompanionRelationshipEnumeration,
)
from generated.discount_basis_enumeration import DiscountBasisEnumeration
from generated.usage_parameter_ref_structure import UsageParameterRefStructure
from generated.usage_parameter_version_structure import (
    UsageParameterVersionStructure,
)
from generated.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompanionProfileVersionStructure(UsageParameterVersionStructure):
    """
    Type for COMPANION PROFILE.

    :ivar parent_ref: Parent USER PROFILE or GROUP TICKET for which this
        specifes the member rules.
    :ivar companion_profile_ref_or_user_profile_ref:
    :ivar companion_relationship_type: Required Relationship of
        companion to eliigble user +V1.1.
    :ivar minimum_number_of_persons: Minimum number of persons of this
        type allowed as companions..
    :ivar maximum_number_of_persons: Maximum number of persons of this
        type allowed as companions.
    :ivar discount_basis: Nature of discount for this profile.
    """

    class Meta:
        name = "CompanionProfile_VersionStructure"

    parent_ref: Optional[UsageParameterRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    companion_relationship_type: Optional[CompanionRelationshipEnumeration] = (
        field(
            default=None,
            metadata={
                "name": "CompanionRelationshipType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    minimum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
