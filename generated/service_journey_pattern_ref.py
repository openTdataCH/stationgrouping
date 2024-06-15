from dataclasses import dataclass

from generated.service_journey_pattern_ref_structure import (
    ServiceJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternRef(ServiceJourneyPatternRefStructure):
    """
    Reference to a SERVICE JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
