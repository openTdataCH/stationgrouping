from dataclasses import dataclass, field
from typing import List, Union

from generated.commercial_profile_eligibility import (
    CommercialProfileEligibility,
)
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.customer_eligibility import CustomerEligibility
from generated.residential_qualification_eligibility import (
    ResidentialQualificationEligibility,
)
from generated.user_profile_eligibility import UserProfileEligibility

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerEligibilitiesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CUSTOMER ELIGIBILITY.s.
    """

    class Meta:
        name = "customerEligibilities_RelStructure"

    choice: List[
        Union[
            ResidentialQualificationEligibility,
            CommercialProfileEligibility,
            UserProfileEligibility,
            CustomerEligibility,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationEligibility",
                    "type": ResidentialQualificationEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibility",
                    "type": CommercialProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibility",
                    "type": UserProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerEligibility",
                    "type": CustomerEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
