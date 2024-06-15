from dataclasses import dataclass

from generated.data_object_subscription_structure import (
    DataObjectSubscriptionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectSubscriptionRequest(DataObjectSubscriptionStructure):
    """
    Request for a subscription to NeTEx Data Object Service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
