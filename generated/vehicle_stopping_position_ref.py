from dataclasses import dataclass

from generated.vehicle_stopping_position_ref_structure import (
    VehicleStoppingPositionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPositionRef(VehicleStoppingPositionRefStructure):
    """
    Reference to a VEHICLE STOPPING POSITION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
