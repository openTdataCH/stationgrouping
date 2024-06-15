from dataclasses import dataclass

from generated.usage_discount_right_version_structure import (
    UsageDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageDiscountRight(UsageDiscountRightVersionStructure):
    """
    A FARE PRODUCT allowing a customer to benefit from discounts when consuming
    VALIDABLE ELEMENTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
