from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.type_of_security_list import TypeOfSecurityList
from generated.type_of_security_list_ref import TypeOfSecurityListRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfSecurityListRelStructure(ContainmentAggregationStructure):
    """Type for a list of TYPE OF SECURITY LISTs.

    +v1.1
    """

    class Meta:
        name = "typesOfSecurityList_RelStructure"

    type_of_security_list_ref_or_type_of_security_list: List[
        Union[TypeOfSecurityListRef, TypeOfSecurityList]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfSecurityListRef",
                    "type": TypeOfSecurityListRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityList",
                    "type": TypeOfSecurityList,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
