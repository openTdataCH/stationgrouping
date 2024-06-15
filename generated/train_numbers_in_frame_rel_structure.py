from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.train_number import TrainNumber
from generated.train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainNumbersInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TRAIN NUMBERs.
    """

    class Meta:
        name = "trainNumbersInFrame_RelStructure"

    train_number_or_train_number_ref: List[
        Union[TrainNumber, TrainNumberRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainNumber",
                    "type": TrainNumber,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
