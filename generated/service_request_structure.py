from dataclasses import dataclass

from generated.contextualised_request_structure import (
    ContextualisedRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceRequestStructure(ContextualisedRequestStructure):
    """
    SIRI Service Request.
    """
