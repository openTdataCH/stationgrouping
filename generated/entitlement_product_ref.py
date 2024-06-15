from dataclasses import dataclass

from generated.entitlement_product_ref_structure import (
    EntitlementProductRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementProductRef(EntitlementProductRefStructure):
    """
    Reference to a ENTITLEMENT PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
