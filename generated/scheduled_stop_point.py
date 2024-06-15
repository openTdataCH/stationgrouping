from dataclasses import dataclass

from generated.scheduled_stop_point_version_structure import (
    ScheduledStopPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledStopPoint(ScheduledStopPointVersionStructure):
    """
    A POINT where passengers can board or alight from vehicles.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
