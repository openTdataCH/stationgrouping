from dataclasses import dataclass

from generated.vehicle_type_version_structure import (
    VehicleTypeVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleType(VehicleTypeVersionStructure):
    """
    Type of VEHICLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
