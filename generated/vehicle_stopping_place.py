from dataclasses import dataclass

from generated.vehicle_stopping_place_version_structure import (
    VehicleStoppingPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlace(VehicleStoppingPlaceVersionStructure):
    """
    Designated PLACE within a STOP PLACE for a VEHICLE to stop.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
