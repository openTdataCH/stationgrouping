from dataclasses import dataclass, field
from typing import Optional

from generated.fare_product_version_structure import (
    FareProductVersionStructure,
)
from generated.usage_discount_right_enumeration import (
    UsageDiscountRightEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageDiscountRightVersionStructure(FareProductVersionStructure):
    """
    Type for USAGE DISCOUNT RIGHT.

    :ivar product_type: Classification of USAGE DISOCUNT RIGHT. +v1.1
    """

    class Meta:
        name = "UsageDiscountRight_VersionStructure"

    product_type: Optional[UsageDiscountRightEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
