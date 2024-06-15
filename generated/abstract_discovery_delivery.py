from dataclasses import dataclass

from generated.abstract_discovery_delivery_structure import (
    AbstractDiscoveryDeliveryStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractDiscoveryDelivery(AbstractDiscoveryDeliveryStructure):
    """
    Abstract type for a discovery delivery.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
