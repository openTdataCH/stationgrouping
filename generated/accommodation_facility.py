from dataclasses import dataclass, field

from generated.accommodation_facility_enumeration import (
    AccommodationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationFacility:
    """Classification of ACCOMMODATION FACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccommodationFacilityEnumeration = field(
        default=AccommodationFacilityEnumeration.SEATING,
        metadata={
            "required": True,
        },
    )
