from dataclasses import dataclass

from generated.simple_feature_version_structure import (
    SimpleFeatureVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleFeature(SimpleFeatureVersionStructure):
    """
    An abstract representation of elementary objects related to the spatial
    representation of the network POINTs (0-dimensional objects), LINKs
    (1-dimensional objects) and ZONEs (2-dimensional objects) may be viewed as
    SIMPLE FEATUREs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
