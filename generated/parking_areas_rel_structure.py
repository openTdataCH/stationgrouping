from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.parking_area import ParkingArea
from generated.parking_area_ref import ParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingAreasRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING AREAs.
    """

    class Meta:
        name = "parkingAreas_RelStructure"

    parking_area_ref_or_parking_area: List[
        Union[ParkingAreaRef, ParkingArea]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
