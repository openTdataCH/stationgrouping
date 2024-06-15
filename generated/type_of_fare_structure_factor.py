from dataclasses import dataclass

from generated.type_of_fare_structure_factor_version_structure import (
    TypeOfFareStructureFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureFactor(TypeOfFareStructureFactorVersionStructure):
    """
    A classification of FARE STRUCTURE FACTORs expressing their general
    functionalities .
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
