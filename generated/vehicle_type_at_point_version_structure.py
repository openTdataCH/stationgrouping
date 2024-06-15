from dataclasses import dataclass, field
from typing import Optional

from generated.network_restriction_version_structure import (
    NetworkRestrictionVersionStructure,
)
from generated.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeAtPointVersionStructure(NetworkRestrictionVersionStructure):
    """
    Type for a VEHICLE TYPE AT POINT.

    :ivar for_vehicle_type_ref: Type of VEHICLE to which NETWORK
        RESTRICTION applies.
    :ivar capacity: Number of vehicles allowed at a point at a given
        time.
    """

    class Meta:
        name = "VehicleTypeAtPoint_VersionStructure"

    for_vehicle_type_ref: VehicleTypeRefStructure = field(
        metadata={
            "name": "ForVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Capacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
