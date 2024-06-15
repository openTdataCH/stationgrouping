from dataclasses import dataclass

from generated.point_of_interest_space_version_structure import (
    PointOfInterestSpaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestSpace(PointOfInterestSpaceVersionStructure):
    """
    A PLACE within a POINT OF INTEREST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
