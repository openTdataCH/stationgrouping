from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from generated.travel_billing_policy_enumeration import (
    TravelBillingPolicyEnumeration,
)
from generated.travel_credit_policy_enumeration import (
    TravelCreditPolicyEnumeration,
)
from generated.usage_parameter_version_structure import (
    UsageParameterVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingPolicyVersionStructure(UsageParameterVersionStructure):
    """
    Type for CHARGING POLICY.

    :ivar credit_policy: Policy for traveling on credit.
    :ivar expire_after_period: Any expiry period on the right to  collec
        a rebate or adjustment.
    :ivar payment_grace_period: Period after purchase by which time
        payment must be settled. +v1.1
    :ivar billing_policy: Policy for billing frequency.
    """

    class Meta:
        name = "ChargingPolicy_VersionStructure"

    credit_policy: Optional[TravelCreditPolicyEnumeration] = field(
        default=None,
        metadata={
            "name": "CreditPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    expire_after_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExpireAfterPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_grace_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PaymentGracePeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    billing_policy: Optional[TravelBillingPolicyEnumeration] = field(
        default=None,
        metadata={
            "name": "BillingPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
