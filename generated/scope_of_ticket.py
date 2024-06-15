from dataclasses import dataclass, field

from generated.ticketing_facility_enumeration import (
    TicketingFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScopeOfTicket:
    """
    Classification of SCOPEs of TICKET, eg national international.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingFacilityEnumeration = field(
        default=TicketingFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
