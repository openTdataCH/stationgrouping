from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFeatureValueStructure(TypeOfEntityVersionStructure):
    """
    Type for a TYPE OF FEATURE.
    """

    class Meta:
        name = "TypeOfFeature_ValueStructure"
