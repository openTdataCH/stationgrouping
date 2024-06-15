from dataclasses import dataclass

from generated.relief_point_version_structure import (
    ReliefPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPoint(ReliefPointVersionStructure):
    """A TIMING POINT where a relief is possible, i.e. a driver may take on or hand
    over a vehicle.

    The vehicle may sometimes be left unattended.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
