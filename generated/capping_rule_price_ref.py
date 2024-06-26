from dataclasses import dataclass

from generated.capping_rule_price_ref_structure import (
    CappingRulePriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappingRulePriceRef(CappingRulePriceRefStructure):
    """
    Reference to a CAPPING RULE PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
