from dataclasses import dataclass

from generated.point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPointAbstract(PointVersionStructure):
    """
    A POINT against which the timing information necessary to build schedules may
    be recorded.
    """

    class Meta:
        name = "TimingPoint_"
        namespace = "http://www.netex.org.uk/netex"
