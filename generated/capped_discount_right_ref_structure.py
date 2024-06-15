from dataclasses import dataclass

from generated.sale_discount_right_ref_structure import (
    SaleDiscountRightRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRightRefStructure(SaleDiscountRightRefStructure):
    """
    Type for Reference to a CAPPED DISCOUNT RIGHT.
    """
