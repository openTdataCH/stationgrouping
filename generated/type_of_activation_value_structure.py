from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfActivationValueStructure(TypeOfEntityVersionStructure):
    """
    Type for a TYPE OF ACTIVATION.
    """

    class Meta:
        name = "TypeOfActivation_ValueStructure"
