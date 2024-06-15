from dataclasses import dataclass

from generated.scheduled_stop_point_derived_view_structure import (
    ScheduledStopPointDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledStopPointView(ScheduledStopPointDerivedViewStructure):
    """Simplified view of SCHEDULED STOP POINT.

    Includes derived some propertries of a stop.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
