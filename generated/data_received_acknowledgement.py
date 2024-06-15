from dataclasses import dataclass

from generated.data_received_response_structure import (
    DataReceivedResponseStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataReceivedAcknowledgement(DataReceivedResponseStructure):
    """Response from Consumer to Producer to acknowledge that data hase been
    received.

    Used as optioanl extra step if reliable delivery is needed. Answers
    a ServiceDelivery.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
