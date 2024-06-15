from dataclasses import dataclass, field
from typing import List

from generated.accommodation_facility_enumeration import (
    AccommodationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationFacilityList:
    """
    List of ACCOMMODATION FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccommodationFacilityEnumeration] = field(
        default_factory=lambda: [
            AccommodationFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
