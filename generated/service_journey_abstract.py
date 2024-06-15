from dataclasses import dataclass

from generated.journey_version_structure import JourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyAbstract(JourneyVersionStructure):
    """
    Dummy SERVICE JOURNEY Supertype.
    """

    class Meta:
        name = "ServiceJourney_"
        namespace = "http://www.netex.org.uk/netex"
