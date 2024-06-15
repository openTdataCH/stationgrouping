from dataclasses import dataclass

from generated.fare_scheduled_stop_point_version_structure import (
    FareScheduledStopPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareScheduledStopPoint(FareScheduledStopPointVersionStructure):
    """
    A POINT where passengers can board or alight from vehicles.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
