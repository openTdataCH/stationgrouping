from dataclasses import dataclass

from generated.timing_link_in_journey_pattern_versioned_child_structure import (
    TimingLinkInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkInJourneyPattern(
    TimingLinkInJourneyPatternVersionedChildStructure
):
    """The position of a TIMING LINK in a JOURNEY PATTERN.

    This ENTITY is needed if a TIMING LINK is repeated in the same
    JOURNEY PATTERN, and separate information is to be stored about each
    iteration of the TIMING LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
