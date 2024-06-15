from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.coupled_journey import CoupledJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CoupledJourneysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  COUPLED JOURNEYs.
    """

    class Meta:
        name = "coupledJourneysInFrame_RelStructure"

    coupled_journey: List[CoupledJourney] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
