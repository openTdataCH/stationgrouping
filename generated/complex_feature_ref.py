from dataclasses import dataclass

from generated.complex_feature_ref_structure import ComplexFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureRef(ComplexFeatureRefStructure):
    """
    Reference to a COMPLEX FEATURE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
