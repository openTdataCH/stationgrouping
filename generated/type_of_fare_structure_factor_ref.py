from dataclasses import dataclass

from generated.type_of_fare_structure_factor_ref_structure import (
    TypeOfFareStructureFactorRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareStructureFactorRef(TypeOfFareStructureFactorRefStructure):
    """
    Reference to a TYPE OF FARE STRUCTURE FACTOR.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
