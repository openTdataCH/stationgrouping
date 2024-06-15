from dataclasses import dataclass

from generated.type_of_service_feature_value_structure import (
    TypeOfServiceFeatureValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfServiceFeature(TypeOfServiceFeatureValueStructure):
    """
    Classification of TYPE OF SERVICE FEATURE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
