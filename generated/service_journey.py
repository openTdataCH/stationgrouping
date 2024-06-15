from dataclasses import dataclass

from generated.service_journey_version_structure import (
    ServiceJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourney(ServiceJourneyVersionStructure):
    """A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE.

    The pattern of working is in principle defined by a SERVICE JOURNEY
    PATTERN. The VIEW includes derived ancillary data from referenced
    entities.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
