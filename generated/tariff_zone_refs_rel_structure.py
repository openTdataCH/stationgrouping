from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.tariff_zone_ref import TariffZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZoneRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TARIFF ZONEs.
    """

    class Meta:
        name = "tariffZoneRefs_RelStructure"

    tariff_zone_ref: List[TariffZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
