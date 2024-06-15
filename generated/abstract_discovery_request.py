from dataclasses import dataclass

from generated.abstract_discovery_request_structure import (
    AbstractDiscoveryRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractDiscoveryRequest(AbstractDiscoveryRequestStructure):
    """
    Abstract Discovery request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
