from dataclasses import dataclass

from generated.type_of_payment_method_value_structure import (
    TypeOfPaymentMethodValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPaymentMethod(TypeOfPaymentMethodValueStructure):
    """Defines an open classification  payment methods.

    + v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
