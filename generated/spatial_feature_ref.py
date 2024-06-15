from dataclasses import dataclass

from generated.group_of_points_ref_structure import GroupOfPointsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpatialFeatureRef(GroupOfPointsRefStructure):
    """
    Reference to a SPATIAL FEATURE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
