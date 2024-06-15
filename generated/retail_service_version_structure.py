from dataclasses import dataclass, field
from typing import List

from generated.local_service_version_structure import (
    LocalServiceVersionStructure,
)
from generated.retail_service_enumeration import RetailServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for RETAIL SERVICE.

    :ivar service_list: RETAIL SERVICEs available.
    """

    class Meta:
        name = "RetailService_VersionStructure"

    service_list: List[RetailServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
