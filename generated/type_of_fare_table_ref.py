from dataclasses import dataclass

from generated.type_of_fare_table_ref_structure import (
    TypeOfFareTableRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareTableRef(TypeOfFareTableRefStructure):
    """
    Reference to a TYPE OF FARE TABLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
