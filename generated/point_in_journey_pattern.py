from dataclasses import dataclass

from generated.point_in_journey_pattern_versioned_child_structure import (
    PointInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointInJourneyPattern(PointInJourneyPatternVersionedChildStructure):
    """
    A STOP POINT or TIMING POINT in a JOURNEY PATTERN with its order in that
    JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
