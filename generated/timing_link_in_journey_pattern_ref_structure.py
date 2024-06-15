from dataclasses import dataclass

from generated.link_in_journey_pattern_ref_structure import (
    LinkInJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkInJourneyPatternRefStructure(LinkInJourneyPatternRefStructure):
    """
    Type for reference to a TIMING LINK JOURNEY PATTERN.
    """
