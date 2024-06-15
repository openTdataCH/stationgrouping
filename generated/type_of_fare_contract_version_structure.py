from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareContractVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF FARE CONTRACT.
    """

    class Meta:
        name = "TypeOfFareContract_VersionStructure"
