from dataclasses import dataclass

from generated.timing_link_in_journey_pattern_ref_structure import (
    TimingLinkInJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkInJourneyPatternRef(TimingLinkInJourneyPatternRefStructure):
    """Reference to a TIMING LINK IN JOURNEY PATTERN.

    If given by context does not need to be stated.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
