from dataclasses import dataclass

from generated.vehicle_stopping_place_ref_structure import (
    VehicleStoppingPlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlaceRef(VehicleStoppingPlaceRefStructure):
    """
    Reference to a VEHICLE STOPPING PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
