from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.type_of_fare_product import TypeOfFareProduct
from generated.type_of_fare_product_ref import TypeOfFareProductRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareProductsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF FARE PRODUCTs.
    """

    class Meta:
        name = "typeOfFareProducts_RelStructure"

    type_of_fare_product_ref_or_type_of_fare_product: List[
        Union[TypeOfFareProductRef, TypeOfFareProduct]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
