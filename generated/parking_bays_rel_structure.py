from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.parking_bay import ParkingBay
from generated.parking_bay_ref import ParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBaysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING BAYs.
    """

    class Meta:
        name = "parkingBays_RelStructure"

    parking_bay_ref_or_parking_bay: List[Union[ParkingBayRef, ParkingBay]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "ParkingBayRef",
                        "type": ParkingBayRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ParkingBay",
                        "type": ParkingBay,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
