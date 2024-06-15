from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLineValueStructure(TypeOfEntityVersionStructure):
    """Type for a TYPE OF LINE.

    +v1.1
    """

    class Meta:
        name = "TypeOfLine_ValueStructure"
