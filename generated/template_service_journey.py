from dataclasses import dataclass

from generated.template_service_journey_version_structure import (
    TemplateServiceJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemplateServiceJourney(TemplateServiceJourneyVersionStructure):
    """
    A VEHICLE JOURNEY with a set of frequencies that may be used to represent a set
    of similar journeys differing only by their time of departure.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
