from dataclasses import dataclass

from generated.scheduled_stop_point_ref_structure import (
    ScheduledStopPointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareScheduledStopPointRefStructure(ScheduledStopPointRefStructure):
    """
    Type for a reference to a FARE SCHEDULED STOP POINT.
    """
