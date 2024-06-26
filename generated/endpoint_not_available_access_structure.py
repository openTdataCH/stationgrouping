from dataclasses import dataclass, field
from typing import Optional

from generated.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EndpointNotAvailableAccessStructure(ErrorCodeStructure):
    """Type for Error: EndpointNotAvailable +SIRI v2.0

    :ivar endpoint: Endpoint that is noit available. + SIRI v2.0
    """

    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
