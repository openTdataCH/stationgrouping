from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareTableVersionStructure(TypeOfValueVersionStructure):
    """
    Type for TYPE OF FARE TABLE.
    """

    class Meta:
        name = "TypeOfFareTable_VersionStructure"
