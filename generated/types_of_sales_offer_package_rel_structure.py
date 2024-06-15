from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.type_of_sales_offer_package import TypeOfSalesOfferPackage
from generated.type_of_sales_offer_package_ref import (
    TypeOfSalesOfferPackageRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfSalesOfferPackageRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF SALES OFFER PACKAGEs.
    """

    class Meta:
        name = "typesOfSalesOfferPackage_RelStructure"

    type_of_sales_offer_package_ref_or_type_of_sales_offer_package: List[
        Union[TypeOfSalesOfferPackageRef, TypeOfSalesOfferPackage]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfSalesOfferPackageRef",
                    "type": TypeOfSalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
