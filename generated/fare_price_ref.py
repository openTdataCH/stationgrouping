from dataclasses import dataclass

from generated.fare_price_ref_structure import FarePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FarePriceRef(FarePriceRefStructure):
    """
    Reference to a FARE PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
