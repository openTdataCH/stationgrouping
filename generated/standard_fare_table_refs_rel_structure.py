from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of FARE STANDARD FARE TABLEs.
    """

    class Meta:
        name = "StandardFareTableRefs_RelStructure"

    standard_fare_table_ref: List[StandardFareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
