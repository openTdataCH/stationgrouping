from dataclasses import dataclass

from generated.subscription_terminated_notification_structure import (
    SubscriptionTerminatedNotificationStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionTerminatedNotification(
    SubscriptionTerminatedNotificationStructure
):
    """
    Notification from Subscriber to Subscription Manager to terminate a
    subscription.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
