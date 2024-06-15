from dataclasses import dataclass, field
from typing import List

from generated.hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireFacilityList:
    """
    List of Hire FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )