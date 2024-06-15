from dataclasses import dataclass

from generated.parking_component_version_structure import (
    ParkingComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingComponent(ParkingComponentVersionStructure):
    """
    Component within a PARKING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
