from dataclasses import dataclass

from generated.service_journey_interchange_ref_structure import (
    ServiceJourneyInterchangeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyInterchangeRef(ServiceJourneyInterchangeRefStructure):
    """
    Reference to a SERVICE JOURNEY INTERCHANGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
