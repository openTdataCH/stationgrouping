from dataclasses import dataclass, field
from typing import List, Union

from generated.capped_discount_right_ref import CappedDiscountRightRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.sale_discount_right_ref import SaleDiscountRightRef
from generated.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DiscountRightRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for list of  references to a DISCOUNT RIGHT.
    """

    class Meta:
        name = "discountRightRefs_RelStructure"

    capped_discount_right_ref_or_sale_discount_right_ref_or_usage_discount_right_ref: List[
        Union[
            CappedDiscountRightRef, SaleDiscountRightRef, UsageDiscountRightRef
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
