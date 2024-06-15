from dataclasses import dataclass

from generated.fare_price_ref_structure import FarePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagePriceRefStructure(FarePriceRefStructure):
    """
    Type for Reference to a CUSTOMER PURCHASE PACKAGE PRICE.
    """
