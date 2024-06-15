from dataclasses import dataclass, field
from typing import List

from generated.family_facility_enumeration import FamilyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FamilyFacilityList:
    """
    List of FAMILY FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[FamilyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
