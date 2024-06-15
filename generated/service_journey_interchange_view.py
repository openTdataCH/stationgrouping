from dataclasses import dataclass

from generated.service_journey_interchange_derived_view_structure import (
    ServiceJourneyInterchangeDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyInterchangeView(
    ServiceJourneyInterchangeDerivedViewStructure
):
    """
    Simplified  view of SERVICE JOURNEY INTERCHANGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
