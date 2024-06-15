from dataclasses import dataclass

from generated.template_service_journey_ref_structure import (
    TemplateServiceJourneyRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemplateServiceJourneyRef(TemplateServiceJourneyRefStructure):
    """
    Reference to a TEMPLATE VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
