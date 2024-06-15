from dataclasses import dataclass, field
from typing import List

from generated.amount_of_price_unit_product_ref import (
    AmountOfPriceUnitProductRef,
)
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AmountOfPriceUnitRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for list of references to an AMOUNT OF PRICE UNIT PRODUCT.
    """

    class Meta:
        name = "amountOfPriceUnitRefs_RelStructure"

    amount_of_price_unit_product_ref: List[AmountOfPriceUnitProductRef] = (
        field(
            default_factory=list,
            metadata={
                "name": "AmountOfPriceUnitProductRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
