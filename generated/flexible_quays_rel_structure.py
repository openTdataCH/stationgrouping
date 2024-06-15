from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.flexible_area_ref import FlexibleAreaRef
from generated.flexible_quay import FlexibleQuay
from generated.flexible_quay_ref import FlexibleQuayRef
from generated.hail_and_ride_area_ref import HailAndRideAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleQuaysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FLEXIBLE QUAYs.
    """

    class Meta:
        name = "flexibleQuays_RelStructure"

    choice: List[
        Union[
            HailAndRideAreaRef, FlexibleAreaRef, FlexibleQuayRef, FlexibleQuay
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuayRef",
                    "type": FlexibleQuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuay",
                    "type": FlexibleQuay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
