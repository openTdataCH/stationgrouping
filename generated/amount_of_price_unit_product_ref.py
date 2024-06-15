from dataclasses import dataclass

from generated.amount_of_price_unit_product_ref_structure import (
    AmountOfPriceUnitProductRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AmountOfPriceUnitProductRef(AmountOfPriceUnitProductRefStructure):
    """
    Reference to a AMOUNT OF PRICE UNIT PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
