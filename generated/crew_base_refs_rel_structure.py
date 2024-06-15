from dataclasses import dataclass, field
from typing import List

from generated.crew_base_ref import CrewBaseRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBaseRefsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CREW BASEs.
    """

    class Meta:
        name = "crewBaseRefs_RelStructure"

    crew_base_ref: List[CrewBaseRef] = field(
        default_factory=list,
        metadata={
            "name": "CrewBaseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
