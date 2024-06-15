from dataclasses import dataclass

from generated.parking_version_structure import ParkingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Parking(ParkingVersionStructure):
    """A named place where Parking may be accessed.

    May be a building complex (e.g. a station) or an on-street location.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
