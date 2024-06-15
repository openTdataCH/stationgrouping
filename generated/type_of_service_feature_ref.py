from dataclasses import dataclass

from generated.type_of_service_feature_ref_structure import (
    TypeOfServiceFeatureRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfServiceFeatureRef(TypeOfServiceFeatureRefStructure):
    """
    Reference to a TYPE OF SERVICE FEATURE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
