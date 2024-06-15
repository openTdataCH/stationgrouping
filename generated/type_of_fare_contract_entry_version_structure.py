from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareContractEntryVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF FARE CONTRACT ENTRY.
    """

    class Meta:
        name = "TypeOfFareContractEntry_VersionStructure"
