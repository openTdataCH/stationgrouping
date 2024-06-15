from dataclasses import dataclass

from generated.vehicle_type_at_point_ref_structure import (
    VehicleTypeAtPointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeAtPointRef(VehicleTypeAtPointRefStructure):
    """
    Reference to an a VEHICLE TYPE AT POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
