from dataclasses import dataclass

from generated.type_of_feature_value_structure import (
    TypeOfFeatureValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFeature(TypeOfFeatureValueStructure):
    """
    TYPE OF FEATURe.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
