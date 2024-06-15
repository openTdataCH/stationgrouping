from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.vehicle_position_alignment import VehiclePositionAlignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePositionAlignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLE POSTION ALIGNMENTs.
    """

    class Meta:
        name = "vehiclePositionAlignments_RelStructure"

    vehicle_position_alignment: List[VehiclePositionAlignment] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePositionAlignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
