from dataclasses import dataclass

from generated.passenger_stop_assignment_ref_structure import (
    PassengerStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignmentRefStructure(
    PassengerStopAssignmentRefStructure
):
    """
    Type for a reference to a VEHICLE JOURNEY STOP ASSIGNMENT.
    """
