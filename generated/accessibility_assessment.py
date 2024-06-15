from dataclasses import dataclass

from generated.accessibility_assessment_versioned_child_structure import (
    AccessibilityAssessmentVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityAssessment(AccessibilityAssessmentVersionedChildStructure):
    """The accessibility characteristics of an entity used by passengers such as a
    STOP PLACE, or a STOP PLACE COMPONENT.

    Described by ACCESSIBILITY LIMITATIONs, and/or a set of
    SUITABILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
