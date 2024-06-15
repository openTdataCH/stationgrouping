from dataclasses import dataclass

from generated.supplement_product_ref_structure import (
    SupplementProductRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplementProductRef(SupplementProductRefStructure):
    """
    Reference to a SUPPLEMENT PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
