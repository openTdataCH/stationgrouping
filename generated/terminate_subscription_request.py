from dataclasses import dataclass

from generated.terminate_subscription_request_structure import (
    TerminateSubscriptionRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminateSubscriptionRequest(TerminateSubscriptionRequestStructure):
    """Request from Subscriber to Subscription Manager to terminate a subscription.

    Answered with a TerminateSubscriptionResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
