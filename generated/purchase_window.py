from dataclasses import dataclass

from generated.purchase_window_version_structure import (
    PurchaseWindowVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurchaseWindow(PurchaseWindowVersionStructure):
    """
    The number and characteristics of persons entitled to use the public transport
    service instead of the original customer.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
