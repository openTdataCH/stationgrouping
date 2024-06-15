from dataclasses import dataclass

from generated.journey_version_structure import JourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyAbstract(JourneyVersionStructure):
    """
    Dummy VEHICLE JOURNEY supertype.
    """

    class Meta:
        name = "VehicleJourney_"
        namespace = "http://www.netex.org.uk/netex"
