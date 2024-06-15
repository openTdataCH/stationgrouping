from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfServiceFeatureValueStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF SERVICE FEATURE.
    """

    class Meta:
        name = "TypeOfServiceFeature_ValueStructure"
