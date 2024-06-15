from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureFactorVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF FARE STRUCTURE FACTOR.
    """

    class Meta:
        name = "TypeOfFareStructureFactor_VersionStructure"
