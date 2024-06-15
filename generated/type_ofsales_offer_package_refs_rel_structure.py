from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.type_of_sales_offer_package_ref import (
    TypeOfSalesOfferPackageRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfsalesOfferPackageRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF SALES OFFER PACKAGE.
    """

    class Meta:
        name = "typeOfsalesOfferPackageRefs_RelStructure"

    type_of_sales_offer_package_ref: List[TypeOfSalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
