from dataclasses import dataclass

from generated.type_of_place_ref_structure import TypeOfPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPlaceRef(TypeOfPlaceRefStructure):
    """
    Reference to a TYPE OF PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
