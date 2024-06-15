from dataclasses import dataclass, field
from typing import Any

from generated.accessibility_limitation_versioned_child_structure import (
    AccessibilityLimitationVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityLimitation(AccessibilityLimitationVersionedChildStructure):
    """
    A categorisation of the ACCESSIBILITY characteristics of a STOP PLACE COMPONENT
    such as a STOP PATH LINK, STOP PLACE or ACCESS SPACE to indicate its usability
    by passengers with specific needs, for example, those needing wheelchair
    access, step-free access or wanting to avoid confined spaces such as lifts.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
