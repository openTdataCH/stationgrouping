from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.routing_constraint_zone import RoutingConstraintZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingConstraintZonesInFrameRelStructure(
    ContainmentAggregationStructure
):
    """
    Type for containment in frame of ROUTING CONSTRAINT ZONE.
    """

    class Meta:
        name = "routingConstraintZonesInFrame_RelStructure"

    routing_constraint_zone: List[RoutingConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )