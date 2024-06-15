from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfVersionValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF VERSION.
    """

    class Meta:
        name = "TypeOfVersion_ValueStructure"
