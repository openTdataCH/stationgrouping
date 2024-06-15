from dataclasses import dataclass

from generated.template_vehicle_journey_version_structure import (
    TemplateVehicleJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TemplateVehicleJourney(TemplateVehicleJourneyVersionStructure):
    """A repeating VEHICLE JOURNEY for which a frequency has been specified, either
    as a HEADWAY JOURNEY GROUP (e.g. every 20 minutes) or a RHYTHMICAL JOURNEY
    GROUP  (e.g. at 15, 27 and 40 minutes past the hour).

    It may thus represent multiple journeys.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
