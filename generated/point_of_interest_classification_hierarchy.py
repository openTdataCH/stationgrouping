from dataclasses import dataclass

from generated.point_of_interest_classification_hierarchy_version_structure import (
    PointOfInterestClassificationHierarchyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestClassificationHierarchy(
    PointOfInterestClassificationHierarchyVersionStructure
):
    """A logical hierarchy for organizing POINT OF INTEREST CLASSIFICATIONs.

    A POINT OF INTEREST CLASSIFICATION can belong to more than one
    hierarchy.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
