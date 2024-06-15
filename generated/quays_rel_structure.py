from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.quay import Quay
from generated.quay_ref import QuayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuaysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of QUAYs.
    """

    class Meta:
        name = "quays_RelStructure"

    quay_ref_or_quay: List[Union[QuayRef, Quay]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
