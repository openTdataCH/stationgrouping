from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.type_of_fare_contract import TypeOfFareContract
from generated.type_of_fare_contract_ref import TypeOfFareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfFareContractRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF FARE CONTRACT s.
    """

    class Meta:
        name = "typesOfFareContract_RelStructure"

    type_of_fare_contract_ref_or_type_of_fare_contract: List[
        Union[TypeOfFareContractRef, TypeOfFareContract]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareContractRef",
                    "type": TypeOfFareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
