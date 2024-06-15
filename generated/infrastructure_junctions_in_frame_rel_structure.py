from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.railway_junction import RailwayJunction
from generated.road_junction import RoadJunction
from generated.wire_junction import WireJunction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureJunctionsInFrameRelStructure(
    ContainmentAggregationStructure
):
    """
    Type for containment in frame of INFRASTRUCTURE POINTs.
    """

    class Meta:
        name = "infrastructureJunctionsInFrame_RelStructure"

    railway_junction_or_road_junction_or_wire_junction: List[
        Union[RailwayJunction, RoadJunction, WireJunction]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RailwayJunction",
                    "type": RailwayJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadJunction",
                    "type": RoadJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireJunction",
                    "type": WireJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
