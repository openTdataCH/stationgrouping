from dataclasses import dataclass

from generated.abstract_service_capabilities_response_structure import (
    AbstractServiceCapabilitiesResponseStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceCapabilitiesResponse(
    AbstractServiceCapabilitiesResponseStructure
):
    """
    Subsititutable type for a SIRI Functional Service Capabilities Response.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
