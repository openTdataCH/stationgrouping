from dataclasses import dataclass

from generated.abstract_service_request_structure import (
    AbstractServiceRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceCapabilitiesRequest(
    AbstractServiceRequestStructure
):
    """
    Subsititutable type for a SIRI Functional Service Capabiloities equest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
