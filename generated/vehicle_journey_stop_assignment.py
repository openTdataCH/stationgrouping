from dataclasses import dataclass

from generated.vehicle_journey_stop_assignment_version_structure import (
    VehicleJourneyStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignment(
    VehicleJourneyStopAssignmentVersionStructure
):
    """
    Change to a PASSENGER STOP ASSIGNMENT for a specific VEHICLE JOURNEY +v1.1.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
