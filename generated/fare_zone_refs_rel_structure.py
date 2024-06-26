from dataclasses import dataclass, field
from typing import List

from generated.fare_zone_ref import FareZoneRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZoneRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of FARE ZONEs.
    """

    class Meta:
        name = "fareZoneRefs_RelStructure"

    fare_zone_ref: List[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
