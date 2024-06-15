from dataclasses import dataclass, field
from typing import List

from generated.route_instruction_version_structure import (
    RouteInstructionVersionStructure,
)
from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteInstructionsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of ROUTE INSTRUCTIONs.

    :ivar route_instruction: A POINT used to define the shape of a ROUTE
        through the network.
    """

    class Meta:
        name = "routeInstructions_RelStructure"

    route_instruction: List[RouteInstructionVersionStructure] = field(
        default_factory=list,
        metadata={
            "name": "RouteInstruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
