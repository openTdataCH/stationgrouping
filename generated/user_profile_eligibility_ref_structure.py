from dataclasses import dataclass

from generated.customer_eligibility_ref_structure import (
    CustomerEligibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileEligibilityRefStructure(CustomerEligibilityRefStructure):
    """
    Type for Reference to a USER PROFILE ELIGIBILITY.
    """
