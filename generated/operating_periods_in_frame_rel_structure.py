from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.operating_period import OperatingPeriod
from generated.uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingPeriodsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of OPERATING PERIODs.
    """

    class Meta:
        name = "operatingPeriodsInFrame_RelStructure"

    operating_period_or_uic_operating_period: List[
        Union[OperatingPeriod, UicOperatingPeriod]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatingPeriod",
                    "type": OperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
