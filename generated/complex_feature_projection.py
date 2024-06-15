from dataclasses import dataclass

from generated.complex_feature_projection_version_structure import (
    ComplexFeatureProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureProjection(ComplexFeatureProjectionVersionStructure):
    """An oriented correspondence:  from one COMPLEX FEATURE in the source layer, onto an entity in a target layer: e.g. POINT, COMPLEX FEATURE,  within a defined TYPE OF PROJECTION."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
