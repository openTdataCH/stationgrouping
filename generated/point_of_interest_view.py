from dataclasses import dataclass

from generated.point_of_interest_derived_view_structure import (
    PointOfInterestDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestView(PointOfInterestDerivedViewStructure):
    """
    Simplified view of POINT OF INTEREST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
