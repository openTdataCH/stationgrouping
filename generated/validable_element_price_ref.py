from dataclasses import dataclass

from generated.validable_element_price_ref_structure import (
    ValidableElementPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementPriceRef(ValidableElementPriceRefStructure):
    """
    Reference to a VALIDABLE ELEMENT PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
