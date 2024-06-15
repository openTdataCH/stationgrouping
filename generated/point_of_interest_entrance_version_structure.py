from dataclasses import dataclass

from generated.site_entrance_version_structure import (
    SiteEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestEntranceVersionStructure(SiteEntranceVersionStructure):
    """
    Type for a POINT OF INTEREST Passenger ENTRANCE.
    """

    class Meta:
        name = "PointOfInterestEntrance_VersionStructure"
