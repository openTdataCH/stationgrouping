from dataclasses import dataclass, field
from typing import Optional

from generated.capping_rules_rel_structure import CappingRulesRelStructure
from generated.sale_discount_right_version_structure import (
    SaleDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRightVersionStructure(SaleDiscountRightVersionStructure):
    """
    Type for CAPPED DISCOUNT RIGHT.

    :ivar capping_rules: Maximum fare to charge.
    """

    class Meta:
        name = "CappedDiscountRight_VersionStructure"

    capping_rules: Optional[CappingRulesRelStructure] = field(
        default=None,
        metadata={
            "name": "cappingRules",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
