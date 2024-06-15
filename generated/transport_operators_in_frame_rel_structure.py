from dataclasses import dataclass, field
from typing import List, Union

from generated.authority import Authority
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.operator import Operator

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportOperatorsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TRANSPORT OPERATORs.
    """

    class Meta:
        name = "transportOperatorsInFrame_RelStructure"

    authority_or_operator: List[Union[Authority, Operator]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
