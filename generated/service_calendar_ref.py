from dataclasses import dataclass

from generated.service_calendar_ref_structure import (
    ServiceCalendarRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceCalendarRef(ServiceCalendarRefStructure):
    """
    Reference to a SERVICE CALENDAR.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
