from dataclasses import dataclass

from generated.fare_product_ref_structure import FareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProductRef(FareProductRefStructure):
    """
    Reference to a FARE PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
