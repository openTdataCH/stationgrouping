from dataclasses import dataclass, field
from typing import List

from generated.safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SafetyFacilityList:
    """
    List of SAFETY FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
