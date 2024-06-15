from dataclasses import dataclass

from generated.service_calendar_frame_ref_structure import (
    ServiceCalendarFrameRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceCalendarFrameRef(ServiceCalendarFrameRefStructure):
    """
    Reference to a SERVICE CALENDAR FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
