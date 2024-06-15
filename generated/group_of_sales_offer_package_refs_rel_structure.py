from dataclasses import dataclass, field
from typing import List

from generated.group_of_sales_offer_packages_ref import (
    GroupOfSalesOfferPackagesRef,
)
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSalesOfferPackageRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a SALES OFFER PACKAGE.
    """

    class Meta:
        name = "groupOfSalesOfferPackageRefs_RelStructure"

    group_of_sales_offer_packages_ref: List[GroupOfSalesOfferPackagesRef] = (
        field(
            default_factory=list,
            metadata={
                "name": "GroupOfSalesOfferPackagesRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
