from dataclasses import dataclass, field
from typing import Optional

from generated.data_object_capabilities_response import (
    DataObjectCapabilitiesResponse,
)
from generated.producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesResponseStructure(ProducerResponseStructure):
    """
    Type for the capabilities of an implementation.
    """

    data_object_capabilities_response: Optional[
        DataObjectCapabilitiesResponse
    ] = field(
        default=None,
        metadata={
            "name": "DataObjectCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
