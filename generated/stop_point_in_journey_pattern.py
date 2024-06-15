from dataclasses import dataclass

from generated.stop_point_in_journey_pattern_versioned_child_structure import (
    StopPointInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPointInJourneyPattern(
    StopPointInJourneyPatternVersionedChildStructure
):
    """The use of a SCHEDULED STOP POINT in a specified order.

    within a JOURNEY PATTERN or SERVICE PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
