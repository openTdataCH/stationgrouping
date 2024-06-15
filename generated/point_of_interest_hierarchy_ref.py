from dataclasses import dataclass

from generated.point_of_interest_hierarchy_ref_structure import (
    PointOfInterestHierarchyRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestHierarchyRef(PointOfInterestHierarchyRefStructure):
    """
    Classification of a POINT OF INTEREST CLASSIFICATION HIERARCHY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
