from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_request_structure import AbstractRequestStructure
from generated.message_qualifier_structure import MessageQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractServiceRequestStructure(AbstractRequestStructure):
    """
    Abstract Service Request for SIRI Service request.

    :ivar message_identifier: Arbitrary unique reference to this
        message.
    """

    message_identifier: Optional[MessageQualifierStructure] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
