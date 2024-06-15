from dataclasses import dataclass

from generated.type_of_fare_structure_element_ref_structure import (
    TypeOfFareStructureElementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureElementRef(TypeOfFareStructureElementRefStructure):
    """
    Reference to a TYPE OF FARE STRUCTURE ELEMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
