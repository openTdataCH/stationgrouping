from dataclasses import dataclass

from generated.customer_eligibility_versioned_child_structure import (
    CustomerEligibilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerEligibility(CustomerEligibilityVersionedChildStructure):
    """Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a
    specific validity Parameter.

    This may be subject to a particular VALIDITY CONDITION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
