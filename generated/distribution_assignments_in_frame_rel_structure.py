from dataclasses import dataclass, field
from typing import List

from generated.distribution_assignment import DistributionAssignment
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionAssignmentsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of DISTRIBUTION ASSIGNMENT.
    """

    class Meta:
        name = "distributionAssignmentsInFrame_RelStructure"

    distribution_assignment: List[DistributionAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DistributionAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
