from dataclasses import dataclass, field
from typing import Optional, Union

from generated.dead_run_ref import DeadRunRef
from generated.journey_headway_versioned_child_structure import (
    JourneyHeadwayVersionedChildStructure,
)
from generated.timing_point_in_journey_pattern_ref import (
    TimingPointInJourneyPatternRef,
)
from generated.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyHeadwayVersionedChildStructure(
    JourneyHeadwayVersionedChildStructure
):
    """
    Type for a VEHICLE JOURNEY FREQUENCY.
    """

    class Meta:
        name = "VehicleJourneyHeadway_VersionedChildStructure"

    dead_run_ref_or_vehicle_journey_ref: Optional[
        Union[DeadRunRef, VehicleJourneyRef]
    ] = field(
        default=None,
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
    timing_point_in_journey_pattern_ref: Optional[
        TimingPointInJourneyPatternRef
    ] = field(
        default=None,
        metadata={
            "name": "TimingPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
