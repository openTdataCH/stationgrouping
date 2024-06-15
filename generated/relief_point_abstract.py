from dataclasses import dataclass

from generated.timing_point_version_structure import (
    TimingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPointAbstract(TimingPointVersionStructure):
    """A TIMING POINT where a relief is possible, i.e. a driver may take on or hand
    over a vehicle.

    The vehicle may sometimes be left unattended.
    """

    class Meta:
        name = "ReliefPoint_"
        namespace = "http://www.netex.org.uk/netex"
