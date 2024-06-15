from dataclasses import dataclass, field
from typing import List, Union

from generated.commercial_profile_eligibility_ref import (
    CommercialProfileEligibilityRef,
)
from generated.customer_eligibility_ref import CustomerEligibilityRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.residential_qualification_eligibility_ref import (
    ResidentialQualificationEligibilityRef,
)
from generated.user_profile_eligibility_ref import UserProfileEligibilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerEligibilityRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of USER PROFILE ELIGIBILITies.
    """

    class Meta:
        name = "customerEligibilityRefs_RelStructure"

    choice: List[
        Union[
            ResidentialQualificationEligibilityRef,
            CommercialProfileEligibilityRef,
            UserProfileEligibilityRef,
            CustomerEligibilityRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationEligibilityRef",
                    "type": ResidentialQualificationEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibilityRef",
                    "type": CommercialProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibilityRef",
                    "type": UserProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerEligibilityRef",
                    "type": CustomerEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
