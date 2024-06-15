from dataclasses import dataclass

from generated.link_in_journey_pattern_versioned_child_structure import (
    LinkInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkInJourneyPattern(LinkInJourneyPatternVersionedChildStructure):
    """
    A SERVICE LINK or TIMING LINK in a JOURNEY PATTERN with its order in that
    JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
