from dataclasses import dataclass

from generated.type_of_fare_contract_version_structure import (
    TypeOfFareContractVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareContract(TypeOfFareContractVersionStructure):
    """
    A classification of FARE CONTRACT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
