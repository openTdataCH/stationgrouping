from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.train_element import TrainElement
from generated.vehicle import Vehicle

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE TYPEs.
    """

    class Meta:
        name = "vehiclesInFrame_RelStructure"

    train_element_or_vehicle: List[Union[TrainElement, Vehicle]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Vehicle",
                    "type": Vehicle,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
