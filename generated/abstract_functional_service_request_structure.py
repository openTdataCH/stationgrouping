from dataclasses import dataclass

from generated.abstract_service_request_structure import (
    AbstractServiceRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceRequestStructure(
    AbstractServiceRequestStructure
):
    """
    Abstract Service Request for SIRI Service request.
    """
