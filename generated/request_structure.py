from dataclasses import dataclass, field
from typing import Optional

from generated.authenticated_request_structure import (
    AuthenticatedRequestStructure,
)
from generated.message_qualifier_structure import MessageQualifierStructure
from generated.participant_ref_structure import ParticipantRefStructure
from generated.requestor_ref import RequestorRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RequestStructure(AuthenticatedRequestStructure):
    """
    Type for General SIRI Request.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar message_identifier: Arbitrary unique identifier that can be
        used to reference this message in subsequent interactions.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. +SIRI 2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: RequestorRef = field(
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    message_identifier: Optional[MessageQualifierStructure] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
