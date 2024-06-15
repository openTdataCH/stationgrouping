from dataclasses import dataclass

from generated.type_of_place_value_structure import TypeOfPlaceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPlace(TypeOfPlaceValueStructure):
    """
    Classification of a PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
