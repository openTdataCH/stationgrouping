from dataclasses import dataclass

from generated.timing_point_in_journey_pattern_versioned_child_structure import (
    TimingPointInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPointInJourneyPattern(
    TimingPointInJourneyPatternVersionedChildStructure
):
    """
    A NODE in a JOURNEY PATTERN which is a TIMING POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
