from dataclasses import dataclass

from generated.preassigned_fare_product_ref_structure import (
    PreassignedFareProductRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplementProductRefStructure(PreassignedFareProductRefStructure):
    """
    Type for Reference to a SUPPLEMENT PRODUCT.
    """
