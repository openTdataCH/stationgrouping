from dataclasses import dataclass, field
from typing import List, Optional

from generated.error_description_structure import ErrorDescriptionStructure
from generated.extensions_1 import Extensions1
from generated.participant_ref_structure import ParticipantRefStructure
from generated.producer_response_structure import ProducerResponseStructure
from generated.subscription_filter_ref_structure import (
    SubscriptionFilterRefStructure,
)
from generated.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionTerminatedNotificationStructure(ProducerResponseStructure):
    """
    Type for Notification to terminate a subscription or subscriptions.

    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar description: Text description providing additional information
        about the reason for the subscription termination.
    :ivar extensions:
    """

    subscriber_ref: List[ParticipantRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: List[SubscriptionFilterRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: List[SubscriptionQualifierStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    description: Optional[ErrorDescriptionStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
