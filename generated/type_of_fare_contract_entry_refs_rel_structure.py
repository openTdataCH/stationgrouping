from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.type_of_fare_contract_entry_ref import (
    TypeOfFareContractEntryRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareContractEntryRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF FARE CONTRACT ENTRY.
    """

    class Meta:
        name = "typeOfFareContractEntryRefs_RelStructure"

    type_of_fare_contract_entry_ref: List[TypeOfFareContractEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
