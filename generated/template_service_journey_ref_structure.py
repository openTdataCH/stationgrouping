from dataclasses import dataclass

from generated.service_journey_ref_structure import ServiceJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemplateServiceJourneyRefStructure(ServiceJourneyRefStructure):
    """
    Type for a reference to a TEMPLATE VEHICLE JOURNEY.
    """
