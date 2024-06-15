from dataclasses import dataclass

from generated.point_of_interest_classification_version_structure import (
    PointOfInterestClassificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestClassification(
    PointOfInterestClassificationVersionStructure
):
    """
    Classification of a POINT OF INTEREST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
