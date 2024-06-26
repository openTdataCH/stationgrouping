from dataclasses import dataclass

from generated.type_of_fare_table_version_structure import (
    TypeOfFareTableVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareTable(TypeOfFareTableVersionStructure):
    """
    Category of FARE TABLE user.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
