from dataclasses import dataclass

from generated.subscription_request_structure import (
    SubscriptionRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionRequest(SubscriptionRequestStructure):
    """Request from Subscriber to Producer for a subscription.

    Answered with a SubscriptionResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
