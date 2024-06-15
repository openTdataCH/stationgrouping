from dataclasses import dataclass

from generated.hail_and_ride_area_version_structure import (
    HailAndRideAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HailAndRideArea(HailAndRideAreaVersionStructure):
    """
    A section of Road between two points within which one may hail a bus to board
    it or alight from it or ask it to stop to alight.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
