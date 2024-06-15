from dataclasses import dataclass, field
from typing import List, Union

from generated.boarding_position import BoardingPosition
from generated.boarding_position_ref import BoardingPositionRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPositionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of BOARDING POSITIONs.
    """

    class Meta:
        name = "boardingPositions_RelStructure"

    boarding_position_ref_or_boarding_position: List[
        Union[BoardingPositionRef, BoardingPosition]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
