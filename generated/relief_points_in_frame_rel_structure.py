from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.garage_point import GaragePoint
from generated.parking_point import ParkingPoint
from generated.relief_point import ReliefPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPointsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of RELIEF POINTs.
    """

    class Meta:
        name = "reliefPointsInFrame_RelStructure"

    parking_point_or_garage_point_or_relief_point: List[
        Union[ParkingPoint, GaragePoint, ReliefPoint]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
