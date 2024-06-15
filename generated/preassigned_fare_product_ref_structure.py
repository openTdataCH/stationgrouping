from dataclasses import dataclass

from generated.fare_product_ref_structure import FareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PreassignedFareProductRefStructure(FareProductRefStructure):
    """
    Type for Reference to a PREASSIGNED FARE PRODUCT.
    """
