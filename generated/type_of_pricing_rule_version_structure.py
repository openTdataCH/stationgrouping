from dataclasses import dataclass, field
from typing import Optional

from generated.tax_category_enumeration import TaxCategoryEnumeration
from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPricingRuleVersionStructure(TypeOfValueVersionStructure):
    """
    Type for TYPE OF PRICING RULE.

    :ivar tax_category: Tax category associated with pricing rule.
    """

    class Meta:
        name = "TypeOfPricingRule_VersionStructure"

    tax_category: Optional[TaxCategoryEnumeration] = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
