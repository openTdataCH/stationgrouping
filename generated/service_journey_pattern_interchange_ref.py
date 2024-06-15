from dataclasses import dataclass

from generated.service_journey_pattern_interchange_ref_structure import (
    ServiceJourneyPatternInterchangeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternInterchangeRef(
    ServiceJourneyPatternInterchangeRefStructure
):
    """
    Reference to a SERVICE JOURNEY PATTERN INTERCHANGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
