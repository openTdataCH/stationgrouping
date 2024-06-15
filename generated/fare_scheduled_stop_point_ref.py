from dataclasses import dataclass

from generated.fare_scheduled_stop_point_ref_structure import (
    FareScheduledStopPointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareScheduledStopPointRef(FareScheduledStopPointRefStructure):
    """
    Reference to a FARE SCHEDULED STOP POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
