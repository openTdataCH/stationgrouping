from dataclasses import dataclass

from generated.capabilities_request_structure import (
    CapabilitiesRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesRequest(CapabilitiesRequestStructure):
    """Requests a the current capabilities of the server.

    Answred with a CpabailitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
