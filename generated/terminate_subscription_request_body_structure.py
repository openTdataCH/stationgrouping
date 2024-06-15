from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.empty_type_1 import EmptyType1
from generated.participant_ref_structure import ParticipantRefStructure
from generated.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminateSubscriptionRequestBodyStructure:
    """Type for Body of Terminate Subscription Request content.

    Used in WSDL.

    :ivar subscriber_ref: Participant identifier of Subscriber.
        Subscription ref will be unique within this.
    :ivar all_or_subscription_ref:
    """

    subscriber_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_or_subscription_ref: List[
        Union[EmptyType1, SubscriptionQualifierStructure]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "All",
                    "type": EmptyType1,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRef",
                    "type": SubscriptionQualifierStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
