from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.flexible_route import FlexibleRoute
from generated.route import Route

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ROUTE.
    """

    class Meta:
        name = "routesInFrame_RelStructure"

    flexible_route_or_route: List[Union[FlexibleRoute, Route]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleRoute",
                    "type": FlexibleRoute,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Route",
                    "type": Route,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
