from dataclasses import dataclass

from generated.usage_discount_right_ref_structure import (
    UsageDiscountRightRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageDiscountRightRef(UsageDiscountRightRefStructure):
    """
    Reference to a USAGE DISCOUNT RIGHT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
