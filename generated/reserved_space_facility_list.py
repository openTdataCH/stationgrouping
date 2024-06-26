from dataclasses import dataclass, field
from typing import List

from generated.reserved_space_facility_enumeration import (
    ReservedSpaceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservedSpaceFacilityList:
    """
    List of RESERVED SPACE FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ReservedSpaceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
