from dataclasses import dataclass

from generated.type_of_fare_structure_element_version_structure import (
    TypeOfFareStructureElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureElement(TypeOfFareStructureElementVersionStructure):
    """
    A classification of FARE STRUCTURE ELEMENTs expressing their general
    functionalities .
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
