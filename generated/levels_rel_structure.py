from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.level import Level
from generated.level_ref import LevelRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of LEVELs.
    """

    class Meta:
        name = "levels_RelStructure"

    level_ref_or_level: List[Union[LevelRef, Level]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LevelRef",
                    "type": LevelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Level",
                    "type": Level,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
