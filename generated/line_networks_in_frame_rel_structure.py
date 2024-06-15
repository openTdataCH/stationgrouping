from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.line_network import LineNetwork

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineNetworksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of LINE NETWORK.

    :ivar line_network: A description of the connectivity of a line as a
        set of LINE SECTIONs. This is sufficient to draw a route map for
        the whole line including branches.
    """

    class Meta:
        name = "lineNetworksInFrame_RelStructure"

    line_network: List[LineNetwork] = field(
        default_factory=list,
        metadata={
            "name": "LineNetwork",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
