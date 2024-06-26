from dataclasses import dataclass

from generated.point_in_journey_pattern_ref_structure import (
    PointInJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPointInJourneyPatternRefStructure(PointInJourneyPatternRefStructure):
    """
    Type for a reference to a STOP POINT IN SEQUENCE.
    """
