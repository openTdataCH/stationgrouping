from dataclasses import dataclass, field
from typing import List

from generated.abstract_subscription_request_structure import (
    AbstractSubscriptionRequestStructure,
)
from generated.data_object_subscription_request import (
    DataObjectSubscriptionRequest,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionRequestStructure(AbstractSubscriptionRequestStructure):
    """
    Type for SIRI Subscription Request.
    """

    data_object_subscription_request: List[DataObjectSubscriptionRequest] = (
        field(
            default_factory=list,
            metadata={
                "name": "DataObjectSubscriptionRequest",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
