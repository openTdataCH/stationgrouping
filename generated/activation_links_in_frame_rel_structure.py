from dataclasses import dataclass, field
from typing import List

from generated.activation_link import ActivationLink
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationLinksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ACTIVATION LINKs.

    :ivar activation_link: A LINK where a control process is activated
        when a vehicle passes it.  Activation links are directional -
        there will be separate links for each direction of a route.
    """

    class Meta:
        name = "activationLinksInFrame_RelStructure"

    activation_link: List[ActivationLink] = field(
        default_factory=list,
        metadata={
            "name": "ActivationLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
