from dataclasses import dataclass, field
from typing import List

from generated.local_service_version_structure import (
    LocalServiceVersionStructure,
)
from generated.money_service_enumeration import MoneyServiceEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for MONEY SERVICE.

    :ivar service_list: MONEY SERVICEs available.
    """

    class Meta:
        name = "MoneyService_VersionStructure"

    service_list: List[MoneyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
