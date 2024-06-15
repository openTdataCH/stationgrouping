from dataclasses import dataclass, field
from typing import List, Union

from generated.garage_point import GaragePoint
from generated.garage_point_ref import GaragePointRef
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePointsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of GARAGEs.
    """

    class Meta:
        name = "garagePoints_RelStructure"

    garage_point_ref_or_garage_point: List[
        Union[GaragePointRef, GaragePoint]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
