from dataclasses import dataclass

from generated.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedVehicleJourneyRefStructure(VehicleJourneyRefStructure):
    """
    Type for a reference to a DATED VEHICLE JOURNEY.
    """
