from dataclasses import dataclass, field
from typing import Optional, Union

from generated.dead_run_ref import DeadRunRef
from generated.journey_layover_structure import JourneyLayoverStructure
from generated.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyLayoverVersionedChildStructure(JourneyLayoverStructure):
    """
    Type for a VEHICLE JOURNEY LAYOVER.
    """

    class Meta:
        name = "VehicleJourneyLayover_VersionedChildStructure"

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
