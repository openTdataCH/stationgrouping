from dataclasses import dataclass

from generated.point_of_interest_classification_derived_view_structure import (
    PointOfInterestClassificationDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestClassificationView(
    PointOfInterestClassificationDerivedViewStructure
):
    """
    Simplified view of POINT OF INTEREST CLASSIFICATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
