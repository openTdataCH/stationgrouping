from dataclasses import dataclass

from generated.traffic_control_point_version_structure import (
    TrafficControlPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrafficControlPoint(TrafficControlPointVersionStructure):
    """A POINT where the traffic flow can be influenced.

    Examples are: traffic lights (lanterns), barriers.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
