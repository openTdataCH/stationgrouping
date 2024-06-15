from dataclasses import dataclass

from generated.type_of_activation_ref_structure import (
    TypeOfActivationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfActivationRef(TypeOfActivationRefStructure):
    """
    Reference to a TYPE OF ACTIVATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
