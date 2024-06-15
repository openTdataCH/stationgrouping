from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.vehicle_model import VehicleModel

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleModelsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE MODELs.
    """

    class Meta:
        name = "vehicleModelsInFrame_RelStructure"

    vehicle_model: List[VehicleModel] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
