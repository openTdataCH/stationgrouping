from dataclasses import dataclass, field

from generated.parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingFacility:
    """
    Classification of PARKING FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ParkingFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
