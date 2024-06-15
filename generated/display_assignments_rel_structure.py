from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.display_assignment import DisplayAssignment
from generated.display_assignment_ref import DisplayAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DisplayAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DISPLAY ASSIGNMENTs.
    """

    class Meta:
        name = "displayAssignments_RelStructure"

    display_assignment_ref_or_display_assignment: List[
        Union[DisplayAssignmentRef, DisplayAssignment]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DisplayAssignmentRef",
                    "type": DisplayAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DisplayAssignment",
                    "type": DisplayAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
