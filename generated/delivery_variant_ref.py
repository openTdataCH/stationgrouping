from dataclasses import dataclass

from generated.delivery_variant_ref_structure import (
    DeliveryVariantRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeliveryVariantRef(DeliveryVariantRefStructure):
    """
    Reference to a DELIVERY VARIANT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
