from dataclasses import dataclass

from generated.parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBay(ParkingBayVersionStructure):
    """
    An individual place to park a VEHICLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
