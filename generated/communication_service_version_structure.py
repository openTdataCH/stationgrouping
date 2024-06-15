from dataclasses import dataclass, field
from typing import List

from generated.communication_service_enumeration import (
    CommunicationServiceEnumeration,
)
from generated.local_service_version_structure import (
    LocalServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommunicationServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for Communication Service.

    :ivar service_list: COMMUNICATION SERVICEs available.
    """

    class Meta:
        name = "CommunicationService_VersionStructure"

    service_list: List[CommunicationServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
