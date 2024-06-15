from dataclasses import dataclass, field
from typing import List

from generated.accessibility_assessment import AccessibilityAssessment
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityAssessmentsRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of ACCESSIBILITY ASSESSMENTs.

    :ivar accessibility_assessment: Assessment of the accessibility of a
        SITE.
    """

    class Meta:
        name = "accessibilityAssessments_RelStructure"

    accessibility_assessment: List[AccessibilityAssessment] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
