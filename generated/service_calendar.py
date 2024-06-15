from dataclasses import dataclass

from generated.service_calendar_version_structure import (
    ServiceCalendarVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceCalendar(ServiceCalendarVersionStructure):
    """A SERVICE CALENDAR.

    A collection of DAY TYPE ASSIGNMENTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
