from dataclasses import dataclass, field
from typing import Optional

from generated.error_code_structure import ErrorCodeStructure
from generated.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownSubscriptionErrorStructure(ErrorCodeStructure):
    """Type for Error: Subscription not found.

    :ivar subscription_code: Ubscription code that could not be found. +
        SIRI v2.0
    """

    subscription_code: Optional[SubscriptionQualifierStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
