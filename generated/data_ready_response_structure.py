from dataclasses import dataclass, field
from typing import Optional, Union

from generated.consumer_response_endpoint_structure import (
    ConsumerResponseEndpointStructure,
)
from generated.error_description_structure import ErrorDescriptionStructure
from generated.other_error import OtherError
from generated.status import Status
from generated.unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataReadyResponseStructure(ConsumerResponseEndpointStructure):
    """
    Type for Data ready Acknowledgement Response.

    :ivar status:
    :ivar error_condition: Description of any error or warning condition
        as to why Consumer cannot fetch data.
    """

    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["DataReadyResponseStructure.ErrorCondition"] = (
        field(
            default=None,
            metadata={
                "name": "ErrorCondition",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )

    @dataclass(kw_only=True)
    class ErrorCondition:
        """
        :ivar unknown_subscription_error_or_other_error:
        :ivar description: Text description of error.
        """

        unknown_subscription_error_or_other_error: Optional[
            Union[UnknownSubscriptionError, OtherError]
        ] = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
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
