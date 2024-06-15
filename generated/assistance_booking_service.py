from dataclasses import dataclass

from generated.assistance_booking_service_version_structure import (
    AssistanceBookingServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceBookingService(AssistanceBookingServiceVersionStructure):
    """
    Information about how to book assistance for wheelchair and disabled users.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
