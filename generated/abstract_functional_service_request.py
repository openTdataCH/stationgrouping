from dataclasses import dataclass

from generated.abstract_functional_service_request_structure import (
    AbstractFunctionalServiceRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceRequest(
    AbstractFunctionalServiceRequestStructure
):
    """
    Subsititutable type for a SIRI Functional Service request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
