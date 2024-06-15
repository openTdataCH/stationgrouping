from dataclasses import dataclass, field
from typing import Optional

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.group_of_timing_links_ref import GroupOfTimingLinksRef
from generated.time_demand_type_ref import TimeDemandTypeRef
from generated.timeband_ref import TimebandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandTypeAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for TIME DEMAND TYPE ASSIGNMENT.
    """

    class Meta:
        name = "TimeDemandTypeAssignment_VersionStructure"

    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timeband_ref: Optional[TimebandRef] = field(
        default=None,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_timing_links_ref: Optional[GroupOfTimingLinksRef] = field(
        default=None,
        metadata={
            "name": "GroupOfTimingLinksRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
