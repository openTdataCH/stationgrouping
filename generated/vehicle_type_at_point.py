from dataclasses import dataclass

from generated.vehicle_type_at_point_version_structure import (
    VehicleTypeAtPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeAtPoint(VehicleTypeAtPointVersionStructure):
    """NETWORK RESTRICTION.

    specifying whether a vehicle of a specified VEHICLE TYPE may visit a
    point.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
