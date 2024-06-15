from dataclasses import dataclass

from generated.sale_discount_right_ref_structure import (
    SaleDiscountRightRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SaleDiscountRightRef(SaleDiscountRightRefStructure):
    """
    Reference to a SALES DISCOUNT RIGHT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
