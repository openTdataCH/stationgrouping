from dataclasses import dataclass

from generated.purchase_window_ref_structure import PurchaseWindowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurchaseWindowRef(PurchaseWindowRefStructure):
    """
    Reference to a PURCHASE WINDOW PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
