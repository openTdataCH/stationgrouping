from dataclasses import dataclass, field
from typing import List

from generated.data_object_request import DataObjectRequest
from generated.service_request_structure import ServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceRequest(ServiceRequestStructure):
    """Request from Consumer to Producer for immediate delivery of data.

    Answered with a ServiceDelivery (or a DataReadyRequest)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    data_object_request: List[DataObjectRequest] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
