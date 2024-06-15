from dataclasses import dataclass

from generated.service_link_in_journey_pattern_versioned_child_structure import (
    ServiceLinkInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkInJourneyPattern(
    ServiceLinkInJourneyPatternVersionedChildStructure
):
    """The use of a SERVICE LINK in a specified order.

    within a JOURNEY PATTERN or SERVICE PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
