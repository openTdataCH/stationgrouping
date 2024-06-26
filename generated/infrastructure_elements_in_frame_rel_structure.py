from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.railway_element import RailwayElement
from generated.road_element import RoadElement
from generated.wire_element import WireElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureElementsInFrameRelStructure(
    ContainmentAggregationStructure
):
    """
    Type for containment in frame of INFRASTRUCTURE LINKs.
    """

    class Meta:
        name = "infrastructureElementsInFrame_RelStructure"

    railway_element_or_road_element_or_wire_element: List[
        Union[RailwayElement, RoadElement, WireElement]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RailwayElement",
                    "type": RailwayElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadElement",
                    "type": RoadElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireElement",
                    "type": WireElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
