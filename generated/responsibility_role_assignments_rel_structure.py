from dataclasses import dataclass, field
from typing import List

from generated.responsibility_role_assignment import (
    ResponsibilityRoleAssignment,
)
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilityRoleAssignmentsRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of RESPONSIBILITY ROLE ASSIGNMENTs.
    """

    class Meta:
        name = "responsibilityRoleAssignments_RelStructure"

    responsibility_role_assignment: List[ResponsibilityRoleAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRoleAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
