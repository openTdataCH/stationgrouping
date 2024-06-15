from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.dynamic_stop_assignment import DynamicStopAssignment
from generated.flexible_stop_assignment import FlexibleStopAssignment
from generated.navigation_path_assignment import NavigationPathAssignment
from generated.passenger_stop_assignment import PassengerStopAssignment
from generated.train_stop_assignment import TrainStopAssignment
from generated.vehicle_journey_stop_assignment import (
    VehicleJourneyStopAssignment,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of STOP ASSIGNMENTs.
    """

    class Meta:
        name = "stopAssignmentsInFrame_RelStructure"

    choice: List[
        Union[
            VehicleJourneyStopAssignment,
            FlexibleStopAssignment,
            NavigationPathAssignment,
            TrainStopAssignment,
            DynamicStopAssignment,
            PassengerStopAssignment,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopAssignment",
                    "type": FlexibleStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathAssignment",
                    "type": NavigationPathAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignment",
                    "type": DynamicStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignment",
                    "type": PassengerStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
