from dataclasses import dataclass

from generated.producer_request_endpoint_structure import (
    ProducerRequestEndpointStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractNotificationStructure(ProducerRequestEndpointStructure):
    """
    Type for Notification Request.
    """
