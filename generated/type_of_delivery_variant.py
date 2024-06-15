from dataclasses import dataclass

from generated.type_of_delivery_variant_value_structure import (
    TypeOfDeliveryVariantValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDeliveryVariant(TypeOfDeliveryVariantValueStructure):
    """
    A classification of DELIVERY VARIANT according to its functional purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
