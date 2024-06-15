from dataclasses import dataclass, field
from typing import Optional

from generated.data_object_capabilities_request import (
    DataObjectCapabilitiesRequest,
)
from generated.request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesRequestStructure(RequestStructure):
    """
    Type for Requests for capabilities of the current system.
    """

    data_object_capabilities_request: Optional[
        DataObjectCapabilitiesRequest
    ] = field(
        default=None,
        metadata={
            "name": "DataObjectCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )
