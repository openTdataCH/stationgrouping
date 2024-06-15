from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.dead_run_ref import DeadRunRef
from generated.dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from generated.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from generated.passenger_stop_assignment_version_structure import (
    PassengerStopAssignmentVersionStructure,
)
from generated.vehicle_journey_ref import VehicleJourneyRef
from generated.vehicle_journey_stop_assignment_ref import (
    VehicleJourneyStopAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignmentVersionStructure(
    PassengerStopAssignmentVersionStructure
):
    """
    Type for VEHICLE JOURNER STOP ASSIGNMENT.
    """

    class Meta:
        name = "VehicleJourneyStopAssignment_VersionStructure"

    dead_run_ref_or_vehicle_journey_ref: List[
        Union[DeadRunRef, VehicleJourneyRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref: Optional[
        Union[
            VehicleJourneyStopAssignmentRef,
            DynamicStopAssignmentRef,
            PassengerStopAssignmentRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
