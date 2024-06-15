from dataclasses import dataclass, field

from generated.vehicle_access_facility_enumeration import (
    VehicleAccessFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessFacility:
    """
    Classification of VEHICLE ACCESS FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: VehicleAccessFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
