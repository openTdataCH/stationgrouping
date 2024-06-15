from dataclasses import dataclass

from generated.timing_point_version_structure import (
    TimingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPoint(TimingPointVersionStructure):
    """
    A POINT against which the timing information necessary to build schedules may
    be recorded.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
