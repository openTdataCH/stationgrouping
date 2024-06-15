from dataclasses import dataclass

from generated.logical_display_version_structure import (
    LogicalDisplayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogicalDisplay(LogicalDisplayVersionStructure):
    """Represents a set of data that can be assembled for assignment to a physical
    PASSENGER INFORMATION EQUIPMENT or to a logical channel such as web or media.

    It is independent of any physical embodiment LOGICAL DISPLAY
    corresponds to a SIRI STOP MONITORING point.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
