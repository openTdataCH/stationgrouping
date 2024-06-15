from dataclasses import dataclass, field
from typing import List

from generated.vehicle_access_facility_enumeration import (
    VehicleAccessFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessFacilityList:
    """
    List of VEHICLE ACCESS FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[VehicleAccessFacilityEnumeration] = field(
        default_factory=lambda: [
            VehicleAccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
