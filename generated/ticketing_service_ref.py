from dataclasses import dataclass

from generated.ticketing_service_ref_structure import (
    TicketingServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingServiceRef(TicketingServiceRefStructure):
    """
    Identifier of an TICKETING SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
