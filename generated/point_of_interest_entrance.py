from dataclasses import dataclass

from generated.point_of_interest_entrance_version_structure import (
    PointOfInterestEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestEntrance(PointOfInterestEntranceVersionStructure):
    """
    Specialisation of ENTRANCE of ENTRANCE for a passenger to a POINT OF INTEREST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
