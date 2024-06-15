from dataclasses import dataclass, field
from typing import Optional

from generated.crew_base_ref import CrewBaseRef
from generated.timing_point_version_structure import (
    TimingPointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPointVersionStructure(TimingPointVersionStructure):
    """
    Type for RELIEF POINT.
    """

    class Meta:
        name = "ReliefPoint_VersionStructure"

    crew_base_ref: Optional[CrewBaseRef] = field(
        default=None,
        metadata={
            "name": "CrewBaseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
