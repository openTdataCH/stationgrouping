from dataclasses import dataclass

from generated.capped_discount_right_ref_structure import (
    CappedDiscountRightRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRightRef(CappedDiscountRightRefStructure):
    """
    Reference to a CAPPED DISCOUNT RIGHT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
