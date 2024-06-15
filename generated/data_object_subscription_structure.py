from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_subscription_structure import (
    AbstractSubscriptionStructure,
)
from generated.data_object_request import DataObjectRequest
from generated.extensions_1 import Extensions1
from generated.network_frame_subscription_policy_structure import (
    NetworkFrameSubscriptionPolicyStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Data type for Subscription Request for  NeTEx Data Object  Service.

    :ivar data_object_request:
    :ivar subscription_policy: Policy to use when processing Network
        Subscriptions.
    :ivar extensions:
    """

    data_object_request: DataObjectRequest = field(
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    subscription_policy: Optional[NetworkFrameSubscriptionPolicyStructure] = (
        field(
            default=None,
            metadata={
                "name": "SubscriptionPolicy",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
