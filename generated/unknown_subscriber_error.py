from dataclasses import dataclass

from generated.unknown_subscriber_error_structure import (
    UnknownSubscriberErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownSubscriberError(UnknownSubscriberErrorStructure):
    """Error: Subscriber not found."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
