from dataclasses import dataclass, field
from typing import List

from generated.response_endpoint_structure import ResponseEndpointStructure
from generated.termination_response_status_structure import (
    TerminationResponseStatusStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminateSubscriptionResponseStructure(ResponseEndpointStructure):
    """
    Type for Response to a request to terminate a subscription or subscriptions.

    :ivar termination_response_status: Status of each subscription
        termnination response.
    """

    termination_response_status: List[TerminationResponseStatusStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "TerminationResponseStatus",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
