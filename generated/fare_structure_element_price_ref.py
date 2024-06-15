from dataclasses import dataclass

from generated.fare_structure_element_price_ref_structure import (
    FareStructureElementPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementPriceRef(FareStructureElementPriceRefStructure):
    """
    Reference to a FARE STRUCTURE ELEMENT PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
