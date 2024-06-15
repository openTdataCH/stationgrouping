from dataclasses import dataclass

from generated.sale_discount_right_version_structure import (
    SaleDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SaleDiscountRight(SaleDiscountRightVersionStructure):
    """
    A FARE PRODUCT allowing a customer to benefit from discounts when purchasing
    SALES OFFER PACKAGEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
