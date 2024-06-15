from dataclasses import dataclass, field
from typing import List, Union

from generated.activation_point import ActivationPoint
from generated.beacon_point import BeaconPoint
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPointsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ACTIVATION POINTs.
    """

    class Meta:
        name = "activationPointsInFrame_RelStructure"

    beacon_point_or_activation_point: List[
        Union[BeaconPoint, ActivationPoint]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
