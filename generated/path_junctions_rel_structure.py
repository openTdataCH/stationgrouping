from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.path_junction import PathJunction
from generated.path_junction_ref import PathJunctionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathJunctionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PATH JUNCTIONs.
    """

    class Meta:
        name = "pathJunctions_RelStructure"

    path_junction_ref_or_path_junction: List[
        Union[PathJunctionRef, PathJunction]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PathJunctionRef",
                    "type": PathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
