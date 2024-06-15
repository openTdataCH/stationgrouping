from dataclasses import dataclass

from generated.assistance_booking_service_ref_structure import (
    AssistanceBookingServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceBookingServiceRef(AssistanceBookingServiceRefStructure):
    """
    Reference to an ASSISTANCE BOOKING SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
