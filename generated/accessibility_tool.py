from dataclasses import dataclass, field

from generated.accessibility_tool_enumeration import (
    AccessibilityToolEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessibilityTool:
    """
    Classification of ACCESSIBILITY TOOLs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessibilityToolEnumeration = field(
        metadata={
            "required": True,
        }
    )
