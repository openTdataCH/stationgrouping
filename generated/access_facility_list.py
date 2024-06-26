from dataclasses import dataclass, field
from typing import List

from generated.access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessFacilityList:
    """
    List of SITE ACCESS FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccessFacilityEnumeration] = field(
        default_factory=lambda: [
            AccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
