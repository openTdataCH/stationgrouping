from dataclasses import dataclass, field
from typing import List

from generated.ticketing_facility_enumeration import (
    TicketingFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingFacilityList:
    """
    List of TICKETING FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
