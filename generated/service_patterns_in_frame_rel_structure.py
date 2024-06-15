from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.journey_pattern_view import JourneyPatternView
from generated.service_pattern import ServicePattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicePatternsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SERVICE PATTERNs.
    """

    class Meta:
        name = "servicePatternsInFrame_RelStructure"

    service_pattern_or_journey_pattern_view: List[
        Union[ServicePattern, JourneyPatternView]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServicePattern",
                    "type": ServicePattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternView",
                    "type": JourneyPatternView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
