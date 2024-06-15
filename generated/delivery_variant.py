from dataclasses import dataclass

from generated.delivery_variant_version_structure import (
    DeliveryVariantVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeliveryVariant(DeliveryVariantVersionStructure):
    """
    A variant text of a NOTICE for use in a specific media or delivery channel
    (voice, printed material, etc).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
