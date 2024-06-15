from dataclasses import dataclass, field
from typing import Optional, Union

from generated.capability_not_supported_error import (
    CapabilityNotSupportedError,
)
from generated.error_description_structure import ErrorDescriptionStructure
from generated.message_qualifier_structure import MessageQualifierStructure
from generated.other_error import OtherError
from generated.participant_ref_structure import ParticipantRefStructure
from generated.response_timestamp import ResponseTimestamp
from generated.status import Status
from generated.subscription_filter_ref_structure import (
    SubscriptionFilterRefStructure,
)
from generated.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)
from generated.unknown_subscriber_error import UnknownSubscriberError
from generated.unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminationResponseStatusStructure:
    """
    Type for Status of termination response.

    :ivar response_timestamp:
    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    """

    response_timestamp: Optional[ResponseTimestamp] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_message_ref: Optional[MessageQualifierStructure] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscriber_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: Optional[SubscriptionFilterRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: Optional[SubscriptionQualifierStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status: Status = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    error_condition: Optional[
        "TerminationResponseStatusStructure.ErrorCondition"
    ] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class ErrorCondition:
        """
        :ivar choice:
        :ivar description: Text description of error.
        """

        choice: Optional[
            Union[
                CapabilityNotSupportedError,
                UnknownSubscriberError,
                UnknownSubscriptionError,
                OtherError,
            ]
        ] = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "CapabilityNotSupportedError",
                        "type": CapabilityNotSupportedError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "UnknownSubscriberError",
                        "type": UnknownSubscriberError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "UnknownSubscriptionError",
                        "type": UnknownSubscriptionError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "OtherError",
                        "type": OtherError,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
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
