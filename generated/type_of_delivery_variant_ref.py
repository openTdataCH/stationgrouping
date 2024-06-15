from dataclasses import dataclass

from generated.type_of_delivery_variant_ref_structure import (
    TypeOfDeliveryVariantRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDeliveryVariantRef(TypeOfDeliveryVariantRefStructure):
    """
    Reference to a TYPE OF DELIVERY VARIANT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
