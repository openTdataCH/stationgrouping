from dataclasses import dataclass

from generated.journey_ref_structure import JourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyRefStructure(JourneyRefStructure):
    """
    Type for a reference to a VEHICLE JOURNEY.
    """
