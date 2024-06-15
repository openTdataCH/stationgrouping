from dataclasses import dataclass

from generated.capped_discount_right_version_structure import (
    CappedDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRight(CappedDiscountRightVersionStructure):
    """
    A FARE PRODUCT allowing a customer to benefit from discounts when consuming
    VALIDABLE ELEMENTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
