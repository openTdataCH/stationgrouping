from dataclasses import dataclass, field

from generated.ticketing_service_facility_enumeration import (
    TicketingServiceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingServiceFacility:
    """Classification of TICKETING FACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingServiceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
