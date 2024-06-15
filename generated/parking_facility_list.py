from dataclasses import dataclass, field
from typing import List

from generated.parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingFacilityList:
    """
    List of PARKING FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ParkingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
