from dataclasses import dataclass, field
from typing import List

from generated.catering_service_enumeration import CateringServiceEnumeration
from generated.local_service_version_structure import (
    LocalServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for CATERING SERVICE.

    :ivar service_list: CATERING SERVICEs available.
    """

    class Meta:
        name = "CateringService_VersionStructure"

    service_list: List[CateringServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
