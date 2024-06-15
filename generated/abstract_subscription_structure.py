from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from generated.participant_ref_structure import ParticipantRefStructure
from generated.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractSubscriptionStructure:
    """
    Type for SIRI Service subscriptions.

    :ivar subscriber_ref: Participant identifier of Subscriber. Normally
        this will be given by context, i.e. be the same as on the
        Subscription Request.
    :ivar subscription_identifier: Identifier to be given to
        Subscription.
    :ivar initial_termination_time: Requested end time for subscription.
    """

    subscriber_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_identifier: SubscriptionQualifierStructure = field(
        metadata={
            "name": "SubscriptionIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    initial_termination_time: XmlDateTime = field(
        metadata={
            "name": "InitialTerminationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
