from dataclasses import dataclass

from generated.vehicle_journey_stop_assignment_ref_structure import (
    VehicleJourneyStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignmentRef(
    VehicleJourneyStopAssignmentRefStructure
):
    """
    Reference to a VEHICLE JOURNEY STOP ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
