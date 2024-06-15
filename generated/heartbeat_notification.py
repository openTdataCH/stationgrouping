from dataclasses import dataclass

from generated.heartbeat_notification_structure import (
    HeartbeatNotificationStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class HeartbeatNotification(HeartbeatNotificationStructure):
    """
    Notification from Producer to Consumer to indicate that the service is running
    normally.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
