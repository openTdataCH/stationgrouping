from dataclasses import dataclass

from generated.complex_feature_version_structure import (
    ComplexFeatureVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeature(ComplexFeatureVersionStructure):
    """
    An aggregate of SIMPLE FEATUREs and/or other COMPLEX FEATUREs; e.g. a STOP AREA
    : combination of STOP POINTs ; a train station : combination of SIMPLE FEATUREs
    (POINTs, LINKs) and COMPLEX FEATUREs (STOP AREAs).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
